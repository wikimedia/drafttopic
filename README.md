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
