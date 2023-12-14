# Draft topic

<blockquote>
⚠️ Warning: As of late 2023, the ORES infrastructure is being deprecated by the
WMF Machine Learning team, please check https://wikitech.wikimedia.org/wiki/ORES for more info.

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
</blockquote>

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

## Generating models

This repository contains a Makefile that will implement the modeling pipeline:

### Generating a single model

You can generate a specific model by asking make to generate it directly. 
```
make models/enwiki.articletopic.gradient_boosting.model
```

### Generating all models

The following command will regenerate the data pipeline for all models in this project. 
```
make models
```

## Generating predictions for a set of page-ids on Wikipedia

For generating topic predictions for a set of revision-ids, download the relevant model and use revscoring's [score](https://github.com/wikimedia/revscoring/blob/master/revscoring/utilities/score.py) utility
to generate predictions. Note that the revision-ids need to be in a file with a format specified by the utility. Use the revision ID of the most recent revision for a page to get a good prediction.
