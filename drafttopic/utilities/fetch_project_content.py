"""
Fetch article and talk page IDs based on embedded wikiproject templates

Usage:
    fetch_project_content --api-host=<url> --mid-level-wp=<path> --output=<path> [--debug]

Options:
    -h --help              Show this documentation.
    --api-host=<url>       The hostname of a Wikipedia (MediaWiki) e.g.
                           "https://en.wikipedia.org/"
    --mid-level-wp=<path>  Mid-level WikiProjects file.
    --output=<path>        Path to a file to write new observations
                           out to. [default: <stdout>]
    --debug                Enable verbose logging.
"""
import json
import logging
import random
import sys
import traceback
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from itertools import islice

import mwapi
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations
from .wikiprojects_common import invert_mid_level_projects,\
    WIKIPROJECT_FETCH_THREADS
from .fetch_page_wikiprojects import fetch_page_wikiprojects


logger = logging.getLogger(__name__)


SAMPLE_PER_PROJECT = 2000
mid_level_categories = "mid_level_categories"


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    session = mwapi.Session(args['--api-host'], user_agent="WikiProjects \
                            fetch_wikiprojects utility.")

    mid_level_wp = None
    try:
        with open(args['--mid-level-wp']) as fwp:
            mid_level_wp = json.loads(fwp.read())
    except:  # noqa: E722
        logger.error("Failed to load mid-level wikiprojects file, check and run\
                    again")
        raise
    mid_level_wp = invert_mid_level_projects(mid_level_wp)

    run(session, output, mid_level_wp)


def run(session, output, mid_level_wp):
    """
    Fetches pages associated with wikiproject templates
    :Parameters:
        session : :class:`mwapi.Session`
            An API session to use for querying
    """
    projects = mid_level_wp["inverse_wp"]
    #projects = ["Wikipedia:WikiProject Education in New Jersey"]
    all_talk_pages = fetch_all_projects_talk_pages(session, projects)

    talk_pages_with_templates = fetch_page_wikiprojects(session, all_talk_pages, mid_level_wp)

    observations = fetch_draft_article_revisions(session, talk_pages_with_templates)

    for ob in observations:
        dump_observation(ob, output)


def fetch_draft_article_revisions(session, observations):
    """
    Find the first revision of associated article page for each talk page and
    add the rev_id to the observation.
    """
    # TODO: chunkify and parallelize
    for ob in observations:
        if not ob['talk_page_title'].startswith('Talk:'):
            logger.warn("Bad talk page {}".format(ob['talk_page_title']))
            continue

        article_name = ob['talk_page_title'][5:]
        doc = session.get(
            action='query',
            titles=article_name,
            prop='revisions',
            rvprop='ids',
            rvlimit=1,
            rvdir='newer',
            formatversion=2)

        try:
            page_documents = doc['query']['pages']
        except (KeyError, IndexError):
            logger.warn("No results returned.")
            continue

        for page_doc in page_documents:
            ob['title'] = page_doc['title']
            for rev_doc in page_doc['revisions']:
                ob['rev_id'] = rev_doc['revid']

            yield ob


def fetch_all_projects_talk_pages(session, projects):
    """
    Return a flattened list of all talk pages tagged with wikiprojects.
    Maximum SAMPLE_PER_PROJECT pages from each project.
    """
    for project_title in projects:
        if not project_title.startswith("Wikipedia:"):
            logger.warn("Malformed project {}".format(project_title))
            continue

        project_name = project_title[10:]
        talk_pages = fetch_project_talk_pages(session, project_name)
        talk_pages = list(talk_pages)

        if len(talk_pages) > SAMPLE_PER_PROJECT:
            # Take a random subset of pages for each project.
            # FIXME: Not sure whether a deterministic sample would be helpful here,
            # because the pages can also change each run due to on-wiki activity.
            talk_pages = random.sample(list(talk_pages), SAMPLE_PER_PROJECT)

        # FIXME: Cheesy way to flatten the output into a single list.
        for observation in talk_pages:
            yield observation


def fetch_project_talk_pages(session, project_name):
    """
    Fetch all talk pages tagged with a given wiki project template.
    """
    template_name = "Template:{}".format(project_name)
    doc = session.get(
        action='query',
        generator='embeddedin',
        geititle=template_name,
        geilimit=500,
        geinamespace=1,
        prop='info',
        formatversion=2,
        continuation=True)

    for result in doc:
        try:
            page_documents = result['query']['pages']
        except (KeyError, IndexError):
            logger.warn("No results returned.")
            continue

        for page_doc in page_documents:
            yield {
                "talk_page_title": page_doc['title'],
                "talk_page_id": page_doc['pageid'],
            }
