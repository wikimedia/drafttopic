# Draft topic

Warning: As of late 2023, the ORES infrastructure is being deprecated by the
WMF  Machine Learning team, please check
https://wikitech.wikimedia.org/wiki/ORES for more info.

While the code in this repository may still work, it is unmaintained, and as
such may break at any time. Special consideration should also be given to
machine learning models seeing drift in quality of predictions.

The replacement for ORES and associated infrastructure is Lift Wing:
https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing

Some Revscoring models from ORES run on the Lift Wing infrastructure, but they
are otherwise unsupported (no new training or code updates).

They can be downloaded from the links documented at:
https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing#Revscoring_models_(migrated_from_ORES)

In the long term, some or all these models *may* be replaced by newer models
specifically tailored to be run on modern ML infrastructure like Lift Wing.

If you have any questions, contact the WMF Machine Learning team:
https://wikitech.wikimedia.org/wiki/Machine_Learning


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
observations, each observation having a **page\_id: \<page-id\>** mapping.
Additionally also pass the mid-level wikiprojects json for the script to
generate wikiprojects to mid-level categories mapping. The script augments the
given list with the mentioned fields, writing them to a new file specified by
**"output"**

## Generating predictions for a set of page-ids on Wikipedia

For generating topic predictions for a set of revision-ids, download the relevant model and use revscoring's [score](https://github.com/wikimedia/revscoring/blob/master/revscoring/utilities/score.py) API
to generate predictions. Note that the revision-ids need to be in a file with a format specified by the API. Use the revision ID of the most recent revision for a page to get a good prediction.
