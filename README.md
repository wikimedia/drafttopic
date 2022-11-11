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
