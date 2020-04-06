"""
``$ drafttopic -h``
::

    This script provides access to a set of utilities for extracting features
    and building draft topic predictors.

    * add_central_africa -- Adds "Geography.Regions.Africa.Central Africa" to
                            the labels manually.
    * balance_sample -- Generates an approximately balances sample of each
                        label
    * extract_from_text -- Extracts features from raw text
    * fetch_article_text -- Gathers current article text for each labeling
                            observation from a MediaWiki API
    * fetch_draft_text -- Gathers first revision article text for each labeling
                          observation from a MediaWiki API
    * taxo_label -- Labels a set of observations based on their
                    WikiProject templates
    * write_labels -- Extracts all labels from a wikiprojects labeled dataset
                      and writes them out to config

    Usage:
        drafttopic (-h | --help)
        drafttopic <utility> [-h | --help]
    Options:
        -h | --help  Prints this documentation
        <utility>    The name of the utility to run
"""
import sys
import traceback
from importlib import import_module


USAGE = """Usage:
    drafttopic (-h | --help)
    drafttopic <utility> [-h | --help]\n"""


def main():

    if len(sys.argv) < 2:
        sys.stderr.write(USAGE)
        sys.exit(1)
    elif sys.argv[1] in ("-h", "--help"):
        sys.stderr.write(__doc__ + "\n")
        sys.exit(1)
    elif sys.argv[1][:1] == "-":
        sys.stderr.write(USAGE)
        sys.exit(1)

    module_name = sys.argv[1]
    try:
        module = import_module(".utilities." + module_name,
                               package="drafttopic")
    except ImportError:
        sys.stderr.write(traceback.format_exc())
        sys.stderr.write("Could not load utility {0}.\n".format(module_name))
        sys.exit(1)

    module.main(sys.argv[2:])
