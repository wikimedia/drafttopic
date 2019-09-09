"""
``$ drafttopic write_labels -h``
::

    Extracts all labels from a wikiprojects labeled dataset and writes them
    out to config.

    Usage:
        write_labels <label> [--input=<path>] [--output=<path>]
                    [--debug]

    Options:
        <label>             Name of the field containing targets
        -h --help           Show this documentation.
        --input=<path>      Path to a file contining observations
                            labels. [default: <stdin>]
        --output=<path>     Path to a file to write labels to.
                            [default: <stdout>]
"""


import json
import logging
import sys
from itertools import chain

from docopt import docopt
from revscoring.utilities.util import read_observations

logger = logging.getLogger(__name__)


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
    label_name = args['<label>']

    config = process_labels(observations, label_name)
    output.write(json.dumps(config, indent=4))
    output.close()


def process_labels(observations, label_name):
    """
    Processes a list of observations given a key and returns a labels-config

    :Parameters:
        observations : `iterable`(`dict`)
            A list of dictionaries containing labels as one of its keys
        label_name : `str`
            The name of the key containing label of interest

    :Returns:
        `dict` : A config dictionary containing a labels key which contains a
        list of labels as required by revscoring
    """
    try:
        labels = [ob[label_name] for ob in observations]
        unique_labels = set(chain(*(l for l in labels)))
        labels = [{"value": label} for label in unique_labels]
        config = {'name': 'drafttopic', 'labels': labels}
        return config
    except KeyError:
        logger.error("Atleast one observation does not contain the label key")
        return None
