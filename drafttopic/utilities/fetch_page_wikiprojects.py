"""

Annotates page_ids with all wikiproject templates
Usage:
    fetch_page_wikiprojects --api-host=<url>
                            --mid_level_wp=<wp>
                            [--input=<path>] [--output=<path>]
                            [--debug] [--verbose]

Options:
    -h --help           Show this documentation.
    --api-host=<url>        The hostname of a Wikipedia (MediaWiki) e.g.
                        "https://en.wikipedia.org/"
    --input=<path>      Path to a file contining observations
                        labels. [default: <stdin>]
    --output=<path>     Path to a file to write new observations
                        (with text) out to. [default: <stdout>]
    --verbose           Prints dots and stuff to stderr
"""


import json
import logging
import sys
import pdb
import traceback
from concurrent.futures import ThreadPoolExecutor
from itertools import islice

import mwapi
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations
from .wikiprojects_common import invert_mid_level_projects


logger = logging.getLogger(__name__)


mid_level_categories = "mid_level_categories"


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    if args['--input'] == '<stdin>':
        observations = read_observations(sys.stdin)
    else:
        observations = read_observations(open(args['--input']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    session = mwapi.Session(args['--api-host'], user_agent="WikiProjects \
                            fetch_wikiprojects utility.")

    mid_level_wp = None
    try:
        with open(args['--mid_level_wp']) as fwp:
            mid_level_wp = json.loads(fwp.read())
    except:
        logger.warn("Failed to load mid-level wikiprojects file, check and run\
                    again")
        pdb.set_trace()
        sys.exit()
    mid_level_wp = invert_mid_level_projects(mid_level_wp)

    verbose = args['--verbose']

    run(session, observations, output, mid_level_wp, verbose)


def run(session, observations, output, mid_level_wp, verbose):

    for ob in fetch_page_wikiprojects(session, observations, verbose=verbose):
        dump_observation(ob, output)


def fetch_page_wikiprojects(session, observations, mid_level_wp,
                            verbose=False):
    """
    Fetches wikiproject templates associated with a page
    :Parameters:
        session : :class:`mwapi.Session`
            An API session to use for querying
        observations : `iterable`(`dict`)
            A collection of observations to annotate
        observations : `iterable`(`dict`)
            A dictionary containing WikiProjects to mid-level categories
            mappings
        verbose : `bool`
            Print dots and stuff
    :Returns:
        An `iterator` of observations augmented with the fields: templates,
        mid_level_categories containing the requested information.
        Note that observations that can't be found will be excluded.
    """
    batches = chunkify(observations, 25)
    executor = ThreadPoolExecutor(max_workers=4)
    _fetch_wikiprojects_info = build_fetch_wikiprojects_info(session)

    for annotated_batch in executor.map(_fetch_wikiprojects_info, batches):
        for annotated_item in annotated_batch:
            yield annotated_item
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
    if verbose:
        sys.stderr.write("\n")


def extract_mid_level_categories(templates, inverse_mid_level_wp):
    mid_level_set = set()
    for tpl in templates:
        template = tpl.replace("Template", "Wikipedia")
        if template in inverse_mid_level_wp:
            mid_level_set.add(inverse_mid_level_wp[template])
    return list(mid_level_set)


def extract_wikiproject_templates(templates):
    """
    Iterates over a list of templates and returns WikiProject related templates
    from them
    """
    wikiprojects = []
    for tpl in templates:
        if tpl['title'].startswith("Template:WikiProject"):
            wikiprojects.append(tpl['title'])
    return wikiprojects


def build_fetch_wikiprojects_info(session, mid_level_wp):

    def _fetch_wikiprojects_info(observations):
        doc = session.get(
            action='query', prop='templates|info', formatversion=2,
            tlnamespace=10, pageids=[ob['page_id'] for ob in observations],
            continuation=True)
        # The above returns a generator for doc, iterating over which we get
        # results for the set of page_ids in batches. We iterate over each
        # such batch to build the info required for each page_id, namely
        # latest_revid and wikiproject templates
        rev_doc_map = {}
        for result in doc:
            for page_doc in result['query']['pages']:
                pageid = page_doc['pageid']
                # seeing the page id for the first time
                if pageid not in rev_doc_map:
                    rev_doc_map[pageid] = \
                        {'page_id': pageid, 'rev_id': page_doc['lastrevid'],
                         'templates': []}
                    if 'templates' in page_doc:
                        rev_doc_map[pageid]['templates'] =\
                            extract_wikiproject_templates(
                                page_doc['templates'])
                # some templates for this pageid were processed in previous
                # batches, update the list with new one's
                else:
                    if 'templates' in page_doc:
                        new_templates = extract_wikiproject_templates(
                            page_doc['templates'])
                        for tpl in new_templates:
                            try:
                                rev_doc_map[pageid]['templates'].append(tpl)
                            except:
                                logger.warn("error in processing templates for\
                                            {0}".format(pageid))
                                pdb.set_trace()
        # All the templates processed for the batch, now generate mid-level
        # categories
        for pageid, doc in rev_doc_map.items():
            doc[mid_level_categories] = \
                extract_mid_level_categories(doc['templates'],
                                             mid_level_wp['inverse_wp'])

        annotated_observations = []
        for ob in observations:
            if ob['page_id'] not in rev_doc_map:
                logger.warn("Could not find information for {0}".format(ob))
            else:
                try:
                    rev_doc = rev_doc_map[ob['page_id']]
                    ob['rev_id'] = rev_doc['rev_id']
                    ob['templates'] = rev_doc['templates']
                    ob[mid_level_categories] = rev_doc[mid_level_categories]
                    annotated_observations.append(ob)
                except:
                    logger.error("Could not process {0}".format(ob))
                    logger.error(traceback.format_exc())
        return annotated_observations
    return _fetch_wikiprojects_info


def chunkify(iterable, size):
    while True:
        output = tuple(islice(iterable, size))
        if output:
            yield output
        else:
            break
