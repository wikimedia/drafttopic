"""
Labels a set of observations based on their WikiProject templates
(expects wp_templates field) using a taxonomy and WikiProject to template name
mapping.

Usage:
    taxo_label (-h --help)
    taxo_label <wp-taxonomy> <wp-templates>
               [--input=<path>] [--output=<path>]
               [--verbose] [--debug]

Options:
    -h --help  Prints this documentation
    <wp-taxonomy>  A yaml file mapping a taxonomy to WikiProjects
    <wp-templates>  A yaml file containing a map of WikiProject name to
                    all possible templates used for tagging.
    --input=<path>   Path to a file containing observations [default: <stdin>]
    --output=<path>  Path to a file to write observations
                     (with taxo "label" field) out to. [default: <stdout>]
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

    wp_taxonomy = yaml.safe_load(open(args['<wp-taxonomy>']))
    wp_templates = yaml.safe_load(open(args['<wp-templates>']))

    if args['--input'] == "<stdin>":
        observations = read_json_lines(sys.stdin)
    else:
        observations = read_json_lines(open(args['--input']))

    if args['--output'] == "<stdout>":
        output = sys.stdout
    else:
        output = open(args['--output'], 'w')

    run(observations, wp_taxonomy, wp_templates, output)


def read_json_lines(f):
    for line in f:
        yield json.loads(line)


def run(observations, wp_taxonomy, wp_templates, output):
    for ob in taxo_label(observations, wp_taxonomy, wp_templates):
        json.dump(ob, output)
        output.write("\n")
        output.flush()


def taxo_label(observations, wp_taxonomy, wp_templates):
    template_to_wp = generate_template_to_wp(wp_templates)
    wp_to_labels = generate_wp_to_labels(wp_taxonomy)

    for i, ob in enumerate(observations):
        label = []
        for template_name in ob['wp_templates']:
            wikiproject_name = template_to_wp.get(template_name.lower())
            label.extend(wp_to_labels.get(wikiproject_name, []))

        ob['taxo_labels'] = label
        yield ob


def generate_template_to_wp(wp_templates):
    template_to_wp = {}
    for wikiproject_name, templates in wp_templates.items():
        for template_name in templates:
            template_to_wp[template_name.lower()] = wikiproject_name

    return template_to_wp


def generate_wp_to_labels(wp_taxonomy):
    wp_to_labels = defaultdict(set)
    for wikiproject_name, label in _invert_wp_taxonomy(wp_taxonomy):
        wp_to_labels[wikiproject_name].add(label)

    return wp_to_labels


def _invert_wp_taxonomy(wp_taxonomy, path=None):
    catch_all = None
    catch_all_wikiprojects = []
    for key, value in wp_taxonomy.items():
        path_keys = (path or []) + [key]
        if key[-1] == "*":
            # this is a catch-all
            catch_all = path_keys
            catch_all_wikiprojects.extend(value)
            continue
        elif isinstance(value, list):
            catch_all_wikiprojects.extend(value)
            for wikiproject_name in value:
                yield wikiproject_name, ".".join(path_keys)
        else:
            yield from _invert_wp_taxonomy(value, path=path_keys)

    if catch_all is not None:
        for wikiproject_name in catch_all_wikiprojects:
            yield wikiproject_name, ".".join(catch_all)
