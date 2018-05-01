# Draft topic

Predicting topics to new drafts based on Wikiprojects on English Wikipedia.

## Setting up

You'll need a working python3 environment, virtualenv is recommended.

Install this library and its requirements using:

```
pip install -r requirements.txt
pip install -e .
```

Download the word2vec data and move to ~/.word2vec/GoogleNews-vectors-negative300.bin.gz
The embeddings are officially available from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

Fetch data, process, and train the model using:
```
make
```
