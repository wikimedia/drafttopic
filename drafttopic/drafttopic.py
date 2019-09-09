"""
``$ drafttopic -h``
::

    This script provides access to a set of utilities for extracting features
    and building draft topic predictors.

    * extract_from_text -- Extracts feature from raw text
    * fetch_page_wikiprojects -- Annotates talk_page_ids with all wikiproject
                                 templates
    * fetch_text -- Gathers text for each labeling observation from a MediaWiki
                    API
    * fetch_wikiprojects -- Generates a machine readable WikiProjects directory
    * trim_wikiprojects -- Generates a mapping of mid-level wikiprojects to
                           list of wikiproject names contained in them
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
