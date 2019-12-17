"""
Generate a balanced sample of labeled articles for a target language.

Usage:
    balance_sample (-h | --help)
    balance_sample <lang> [-n=<num>]
                   [--input=<path>] [--output=<path>]

Options:
    -h --help  Prints this documentation
    <lang>     Language code to target
    -n=<num>   The number of labels per class to target [default: 1000]
    --input=<path>   Observation containing the target labels.
    --output=<path>  Path to a file to write labels to.
                     [default: <stdout>]
"""
import json
import logging
import random
import sys
from collections import defaultdict

from docopt import docopt
from revscoring.utilities.util import read_observations

logger = logging.getLogger(__name__)


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s')

    lang_code = args['<lang>']
    max_n = int(args['-n'])

    if args['--input'] == '<stdin>':
        observations = read_observations(sys.stdin)
    else:
        observations = read_observations(open(args['--input']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    balance_sample(observations, lang_code, max_n, output)


def balance_sample(observations, lang_code, max_n, output):
    label_obs = group_labeled_obs(observations, lang_code)

    for taxo_label, obs in label_obs.items():
        if len(obs) < max_n:
            logger.warning("Only found {0} observations for {1}"
                           .format(len(obs), taxo_label))
            sampled_obs = obs
        else:
            sampled_obs = random.sample(obs, max_n)

        for ob in sampled_obs:
            output.write(json.dumps(ob) + "\n")


def group_labeled_obs(observations, lang_code):
    label_obs = defaultdict(list)
    for ob in observations:
        if lang_code in ob['sitelinks']:
            labeled_ob = {
                'title': ob['sitelinks'][lang_code],
                'taxo_labels': ob['taxo_labels']}
            for taxo_label in ob['taxo_labels']:
                label_obs[taxo_label].append(labeled_ob)
    return label_obs
