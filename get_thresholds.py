"""
Queries for optimal thresholds from ORES.


Usage:
    get_thresholds (-h|--help)
    get_thresholds <wiki> <model>

Options:
    -h --help  Prints this documentation
    <wiki>     The DBname of the wiki to query thresholds for.
    <model>    The name of the model to get thresholds for.
"""
import docopt
import requests
from tabulate import tabulate

ORES_HOST = "https://ores.wikimedia.org"
PATH = "/v3/scores"
PRECISION_TARGETS = [0.7, 0.5, 0.3, 0.15]


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    wiki = args['<wiki>']
    model = args['<model>']

    headers = [['label', 'pop rate', 'threshold', 'precision', 'recall']]

    table_data = headers
    for label, pop_rate in get_labels(wiki, model):
        threshold, precision, recall = get_best_threshold(wiki, model, label)
        row = [label, pop_rate, threshold, precision, recall]
        table_data.append(row)

    print(tabulate(table_data))


def get_labels(wiki, model):
    doc = requests.get(
        ORES_HOST + PATH + "/" + wiki + "/",
        params={
            'models': model,
            'model_info': "params|statistics.rates"
        }
    ).json()
    model_doc = doc[wiki]['models'][model]
    labels = model_doc['params']['labels']
    pop_rates = model_doc['statistics']['rates']['population']
    return [(l, pop_rates[l]) for l in labels]


def get_threshold(wiki, model, label, target):
    doc = requests.get(
        ORES_HOST + PATH + "/" + wiki + "/",
        params={
            'models': model,
            'model_info': "statistics.thresholds.{0}".format(repr(label)) +
                          ".'maximum recall @ precision >= {0}'".format(target)
        }
    ).json()

    thresholds = doc[wiki]['models'][model]['statistics']['thresholds'][label]
    if len(thresholds) == 1 and thresholds[0] is not None:
        return thresholds[0]['threshold'], thresholds[0]['recall']
    else:
        return None, None


def get_best_threshold(wiki, model, label):
    for target in PRECISION_TARGETS:
        threshold, recall = get_threshold(wiki, model, label, target)
        if recall is not None and recall >= 0.5:
            return threshold, target, recall

    return 0.9, "< 0.15", None


if __name__ == '__main__':
    main()
