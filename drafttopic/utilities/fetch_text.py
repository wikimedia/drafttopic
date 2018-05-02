"""
    Fetches text for labelings using a MediaWiki API.
    Usage:
        fetch_text --api-host=<url> [--labelings=<path>] [--output=<path>]
                                    [--verbose]

    Options:
        -h --help           Show this documentation.
        --api-host=<url>    The hostname of a MediaWiki e.g.
                            "https://en.wikipedia.org"
        --labelings=<path>  Path to a containting observations with extracted
                            labels. [default: <stdin>]
        --output=<path>     Path to a file to write new observations
                            (with text) out to. [default: <stdout>]
        --verbose           Prints dots and stuff to stderr
"""
import logging
import re
import sys
from itertools import islice
from concurrent.futures import ThreadPoolExecutor

import mwapi
from mw.lib import title as mwtitle
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations
from .wikiprojects_common import WIKIPROJECT_FETCH_THREADS


logger = logging.getLogger(__name__)
REDIRECT_RE = re.compile("#redirect", re.I)


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    if args['--labelings'] == '<stdin>':
        labelings = read_observations(sys.stdin)
    else:
        labelings = read_observations(open(args['--labelings']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    session = mwapi.Session(args['--api-host'],
                            user_agent="Drafttopic fetch_text utility.")

    verbose = args['--verbose']

    run(labelings, output, session, verbose)


def run(labelings, output, session, verbose):
    for ob in fetch_text(session, labelings, verbose):
        dump_observation(ob, output)


def fetch_text(session, labelings, verbose=False):
    """
    Fetches article text for labelings from a MediaWiki API.
    :Parameters:
        session : :class:`mwapi.Session`
            An API session to use for querying
        labelings : `iterable`(`dict`)
            A collection of labeling events to add text to
        verbose : `bool`
            Print dots and stuff
    :Returns:
        An `iterator` of labelings augmented with 'text'.  Note that labelings
        of articles that aren't found will not be
        included.
    """

    batches = chunkify(labelings, 25)
    executor = ThreadPoolExecutor(max_workers=WIKIPROJECT_FETCH_THREADS)
    _fetch_text = build_fetch_text_extractor(session)

    for annotated_batch in executor.map(_fetch_text, batches):
        for annotated_item in annotated_batch:
            yield annotated_item
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
    if verbose:
        sys.stderr.write("\n")


def build_fetch_text_extractor(session):

    def _fetch_text(labelings):
        docs = session.get(
            action="query", prop="revisions", rvprop=["content"],
            redirects=True, titles=[ob['talk_page_title'] for ob in labelings],
            continuation=True, formatversion=2
        )
        rev_doc_map = {}
        for result in docs:
            page_documents = None
            try:
                page_documents = result['query']['pages']
            except (KeyError, IndexError):
                logger.warn("No results returned.")
                continue
            for page_doc in page_documents:
                try:
                    text = page_doc['revisions'][0]['content']
                    if is_article(text):
                        title = mwtitle.normalize(page_doc['title'])
                        rev_doc_map[title] = text
                except (KeyError, IndexError):
                    continue

        augmented_observations = []
        for ob in labelings:
            title = ob['talk_page_title']
            ob['text'] = ''
            if mwtitle.normalize(title) in rev_doc_map:
                ob['text'] = rev_doc_map[title]
            else:
                sys.stderr.write("?")
                sys.stderr.write(title)
                sys.stderr.flush()

            augmented_observations.append(ob)
        return augmented_observations
    return _fetch_text


def is_article(text):
    return not (text is None or
                len(text) < 50 or
                REDIRECT_RE.match(text))


def chunkify(iterable, size):
    while True:
        output = tuple(islice(iterable, size))
        if output:
            yield output
        else:
            break
