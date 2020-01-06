"""
``$ drafttopic write_labels -h``
::

    Extracts all potential labels from a taxonomy.

    Usage:
        write_labels (-h | --help)
        write_labels <label> [--input=<path>] [--output=<path>]
                    [--debug]

    Options:
        -h --help        Show this documentation.
        <label>          The target label field name
        --input=<path>   Observation containing the target labels.
                         [default: <stdin>]
        --output=<path>  Path to a file to write labels to.
                         [default: <stdout>]
        --debug          Print debug logs.
"""


import json
import logging
import sys
from collections import defaultdict

from docopt import docopt
from revscoring.utilities.util import read_observations

logger = logging.getLogger(__name__)


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )
    label_field = args['<label>']

    if args['--input'] == '<stdin>':
        observations = read_observations(sys.stdin)
    else:
        observations = read_observations(open(args['--input']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    write_labels(observations, label_field, output)


def write_labels(observations, label_field, output):
    labels_config = process_labels(observations, label_field)
    json.dump(labels_config, output)
    output.close()


def process_labels(observations, label_field):
    label_counts = defaultdict(int)
    total_labels = 0
    for ob in observations:
        labels = ob[label_field]
        for label in labels:
            label_counts[label] += 1
            total_labels += 1

    labels_config = {"name": label_field, "labels": []}
    for label in sorted(label_counts.keys()):
        count = label_counts[label]
        labels_config['labels'].append({
            'value': label,
            'population_rate': count / total_labels})

    return labels_config
