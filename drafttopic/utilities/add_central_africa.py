"""
Adds "Geography.Regions.Africa.Central Africa" to the labels manually.  This is
necessary to deal with a gap in the WikiProject page matching logic.   For various
reasons, very few pages get tagged as being topical to Central Africa.  This
script ensures that at least *some* articles get tagged as topically relevant.

Usage:
    add_central_africa (-h --help)
    add_central_africa [--input=<path>] [--output=<path>]
		       [--titles=<path>]
                       [--verbose] [--debug]

Options:
    -h --help  Prints this documentation
    --input=<path>   Path to a file containing observations [default: <stdin>]
    --output=<path>  Path to a file to write observations
                     (with taxo "label" field) out to. [default: <stdout>]
    --titles=<path>  The path to a file containing a set of enwiki titles that
		     should be categorized under Central Africa.
		     [default: datasets/enwiki.central_africa_titles.txt]
    --verbose  Print progress log
    --debug    Print debug logging
"""
import json
import logging
import sys
from collections import defaultdict

import docopt
import yaml


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.DEBUG if args['--debug'] else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    if args['--input'] == "<stdin>":
        observations = read_json_lines(sys.stdin)
    else:
        observations = read_json_lines(open(args['--input']))

    if args['--output'] == "<stdout>":
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    titles = set(line.strip() for line in open(args['--titles']))
    verbose = args['--verbose']

    run(observations, titles, output, verbose)


def read_json_lines(f):
    for line in f:
        yield json.loads(line)


def run(observations, titles, output, verbose=False):
    for ob in observations:
        if isinstance(ob['sitelinks'], dict) and ob['sitelinks'].get('en') in titles:
            ob['taxo_labels'].append('Geography.Regions.Africa.Central Africa')
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
        output.write(json.dumps(ob))
        output.write("\n")
        output.flush()
