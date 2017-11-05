# Draft topic

Predicting topics to new drafts based on Wikiprojects on English Wikipedia.

## Setting up

Make sure to have a working python3 environment.
Install requirements using:

```
pip install -r requirements
```

Install the library using:

```
python setup.py install
```

## Generating machine-readable WikiProjects data

Use the following utility from root directory to generate machine-readable WikiProjects data:

```
./utility fetch_wikiprojects --output <output_file_name.json>
```

## Generating mid-level category to WikiProjects mapping

Use the following utility from root directory to generate a mapping of high-level topic categories to list of WikiProjects contained in them:

```
./utility trim_wikiprojects --wikiprojects wp --output outmid
```

## Labeling a list of page-ids with the wikiprojects and mid-level categories each page belongs to

Use the following utility from root directory to label a list of page-ids with the wikiprojects and the mid-level categories the page belongs to.

```
./utility fetch_page_wikiprojects --api-host=https://en.wikipedia.org/ --input=wikiproject_page_ids.json --output=enwiki.labeled_wikiprojects.json --mid_level_wp=outmid.json --verbose
```

In above, the input to the script should be a json containing a list of
observations, each observation having a **page\_id: <page-id>** mapping.
Additionally also pass the mid-level wikiprojects json for the script to
generate wikiprojects to mid-level categories mapping. The script augments the
given list with the mentioned fields, writing them to a new file specified by
<output>
