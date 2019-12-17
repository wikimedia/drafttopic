"""
``$ drafttopic fetch_text -h``
::

    Fetches initial draft text for observations using a MediaWiki API.

    Usage:
        fetch_draft_text --api-host=<url>
                         [--input=<path>] [--output=<path>]
                         [--thread=<num>] [--debug]

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
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import mwapi
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations

logger = logging.getLogger(__name__)
REDIRECT_RE = re.compile("#redirect", re.I)
DRAFTTOPIC_UA = "Drafttopic fetch_text <ahalfaker@wikimedia.org>"


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
    for obs in fetch_draft_texts(observations, session, threads):
        dump_observation(obs, output)


def fetch_draft_texts(observations, session, threads):
    """
    Fetches draft (first revision) text for observations from a MediaWiki API.
    """

    executor = ThreadPoolExecutor(max_workers=threads)
    _fetch_draft_text = build_fetch_text(build_get_first_revision(session))

    for obs in executor.map(_fetch_draft_text, observations):
        if obs is not None:
            yield obs
            logger.debug("Write {0} with {1} chars of text."
                         .format(obs['title'], len(obs['text'])))


def build_fetch_text(get_first_revision):

    def _fetch_text(obs):
        result = get_first_revision(obs['title'])
        try:
            page_documents = result['query']['pages']
        except (KeyError, IndexError):
            logger.warn("Could not look up revision for {0}"
                        .format(obs['title']))
            return None
        for page_doc in page_documents:
            try:
                rev_doc = page_doc['revisions'][0]
                text = rev_doc['content']
                if is_article(text):

                    obs['text'] = text
                    obs['title'] = page_doc['title']
                    obs['rev_id'] = rev_doc['revid']

                    return obs
                else:
                    logger.warn("{0} doesn't look like article text: {1}"
                                .format(obs['title'], text[:20]))

            except (KeyError, IndexError) as e:
                logger.error("Something went wrong while processing {0}: {1}"
                             .format(obs['title'], e))
                return None

    return _fetch_text


def is_article(text):
    return not (text is None or
                len(text) < 50 or
                REDIRECT_RE.match(text))


def build_get_first_revision(session):
    def get_first_revision(title):
        return session.get(
            action="query",
            prop="revisions",
            rvprop=["content", "ids"],
            titles=title,
            redirects=True,
            rvlimit=1,
            rvdir="newer",
            formatversion=2
        )


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
