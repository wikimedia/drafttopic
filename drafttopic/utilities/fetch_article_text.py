"""
``$ drafttopic fetch_text -h``
::

    Fetches initial draft text for observations using a MediaWiki API.

    Usage:
        fetch_draft_text --api-host=<url>
                         [--input=<path>] [--output=<path>]
                         [--threads=<num>] [--debug]

    Options:
        -h --help           Show this documentation.
        --api-host=<url>    The hostname of a MediaWiki e.g.
                            "https://en.wikipedia.org"
        --input=<path>      Path to a containting observations with extracted
                            labels. [default: <stdin>]
        --output=<path>     Path to a file to write new observations
                            (with text) out to. [default: <stdout>]
        --threads=<num>     The number of parallel query threads to run
                            [default: 4]
        --debug             Print debug logging
"""
import logging
import sys
from concurrent.futures import ThreadPoolExecutor

import mwapi
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations

from .fetch_draft_text import DRAFTTOPIC_UA, build_fetch_text

logger = logging.getLogger(__name__)


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s')

    if args['--input'] == '<stdin>':
        observations = read_observations(sys.stdin)
    else:
        observations = read_observations(open(args['--input']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    threads = int(args['--threads'])

    session = mwapi.Session(args['--api-host'],
                            user_agent=DRAFTTOPIC_UA)

    run(observations, session, threads, output)


def run(observations, session, threads, output, verbose):
    for obs in fetch_article_texts(observations, session, threads):
        dump_observation(obs, output)


def fetch_article_texts(observations, session, threads):
    """
    Fetches article (recent revision) text for observations from a
    MediaWiki API.
    """

    executor = ThreadPoolExecutor(max_workers=threads)
    _fetch_article_text = build_fetch_text(build_get_recent_revision(session))

    for obs in executor.map(_fetch_article_text, observations):
        if obs is not None:
            yield obs
            logger.debug("Write {0} with {1} chars of text."
                         .format(obs['title'], len(obs['text'])))


def build_get_recent_revision(session):
    def get_recent_revision(title):
        return session.get(
            action="query",
            prop="revisions",
            rvprop=["content", "ids"],
            titles=title,
            redirects=True,
            rvlimit=1,
            rvdir="older",
            formatversion=2
        )
    return get_recent_revision
