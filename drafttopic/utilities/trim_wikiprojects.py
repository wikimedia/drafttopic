"""
Generates a mapping of mid-level wikiprojects to list of wikiproject names
contained in them
{
    'Music': ['Wikipedia: WikiProject Composer', 'Wikipedia: WikiProject Music
    Theory'...]
    .
    .
    .
}

Usage:
    trim_wikiprojects --wikiprojects <wp> [--output=<path>] [--debug]
    [--ignore-inactive]

Options:
    --wikiprojects        Path to wikiprojects json file
    --output=<path>       Path to an file to write output to
                          [default: <stdout>]
    --debug               Print debug logging
    --ignore-inactive     Ignore list of inactive WikiProjects
"""

import json
import logging
import docopt
import sys
from .fetch_wikiprojects import wpd_page, WikiProjectsParser


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.DEBUG if args['--debug'] else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )
    wps = args['<wp>']
    if args['--output'] == "<stdout>":
        output_f = sys.stdout
    else:
        output_f = open(args['--output'], "w")
    run(output_f, wps)


def run(output, wikiprojectsfile):
    logger = logging.getLogger(__name__)
    parser = WikiProjectsParser(wpd_page, logger)
    wps = {}
    try:
        f = open(wikiprojectsfile, 'r')
        wikiprojects = json.loads(f.read())
        f.close()
    except IOError as e:
        logger.warn("Failed to read wikiprojects file")
        return
    wps = parser.parse_mid_level(wikiprojects)
    output.write(json.dumps(wps, indent=4))
