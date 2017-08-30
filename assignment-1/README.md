# Assignment 1

The task is to implement document retrieval methods and evaluate them using a standard test collection.

The assignment consists of three main parts.

For each part a skeleton of the code are provided as Jupyter notebooks. These notebooks are pushed to the private GitHub repositories. Make sure you work with the files in your private repo.


## Part 1 (week 35)

  - Download the document collection and index it using Elasticsearch.
    * Use two fields, title and content.
    * See [this page](https://github.com/kbalog/uis-dat630-fall2017/tree/master/elasticsearch) for help on Elasticsearch.
    * See [below](#document-collection) for details about the document collection.
    * The [1_Indexer.ipynb](1_Indexer.ipynb) notebook contains the code that you need to complete.
  - Perform a baseline retrieval using the default retrieval model in Elasticsearch (which is BM25).
    * Search only in the content field.
    * Return the top 100 documents for each query in `data/queries.txt` and write the results to a file (see [below](#output-file-format) for the output file format).
    * The [2_Baseline_retrieval.ipynb](2_Baseline_retrieval.ipynb) notebook contains the code that you need to complete.


## Part 2 (week 36)

  - Evaluate the performance of the baseline retrieval model in terms of Mean Average Precision (MAP), Precision@10 (P10), and Mean Reciprocal Rank (MRR).
  - Implement the Mixture of Language Models (MLM) approach with two fields (title and content).
    * For each query, obtain the top 200 documents using the default Elasticsearch model (using the "content" field only), then re-rank these documents by computing the MLM score for each (and then return the top 100).


## Part 3 (week 37)

  - Find the parameter setting that yields the best performance.
    * For BM25, tune the k1 and b parameters.
    * For MLM, tune the field weights, smoothing method, and smoothing parameter.
  - You need to reach a **MAP score of minimum 0.07** in order to pass this assignment.
    * *[NOTE] This value might change.*
  - Perform a query-level comparison between the baseline BM25 model (with default parameter settings) and the MLM approach (with the best parameters).
  - You may compete with a single ranking against other teams.
    * The best performing team (each team member) will get 5 bonus points at the final exam.
    * *Details and submission link are coming soon.*


## Deliverable

  - **Submission deadline: 18/09 10:00**. This is an absolute, immutable deadline.
  - *Details are coming soon.*


## Data

### Document collection

The AQUAINT document collection consists of newswire text data in English, drawn from three sources: the Xinhua News Service (`xie`), the New York Times News Service (`nyt`), and the Associated Press Worldstream News Service (`apw`). It has been used in official benchmark evaluations conducted by National Institute of Standards and Technology (NIST).

The text data are separated into directories by source (`apw`, `nyt`, `xie`); within each source, data files are subdivided by year, and within each year, there is one file per date of collection. Each file contains a stream of SGML-tagged text, i.e., blocks of text bounded by `<DOC>` and `</DOC>` tags.  Create an index with *title* (inside `<HEADING>`) and *content* fields (inside `<TEXT>`) and use `<DOCNO>` as the document identifier (docID).

The collection is 1.1GB compressed and can be dowloaded from here: http://www.ux.uis.no/~balog/dat630/aquaint.zip

Upon successful indexing, the index should contain 1,033,461 documents. (Assuming your index is called "aquaint", you can check it at http://localhost:9200/aquaint/_stats.)

You are requested to delete the collection after this assignment.


### Queries

The [queries.txt](data/queries.txt) file contains 50 queries in total.  Each line starts with a 3-digit queryID, followed by the query string.  E.g.,

```
336 Black Bear Attacks
341 Airport Security
...
```


### Relevance judgments

The [qrels2.csv](data/qrels2.csv) file contains the relevance judgments for all queries. Each line contains a queryID and the set of docIDs. The queryID and docIDs are separated by a comma, the docIDs are separated by spaces. (Note that relevance is binary, so the order in which these documents are listed does not matter.)

The new qrels file (qrels2.csv) contains only 45 queries, i.e., for 5 queries there are no relevance assessments. Just ignore those queries that are not in qrels2.csv when computing the MAP scores.

```
queryID,docIDs
303,APW19980610.1778 APW19990525.0223 APW19990602.0039  ...
307,APW19980602.0026 APW19980603.0021 APW19980810.1038 ...
...
```


### Output file format

For every query in queries.txt, the output file should contain two columns: queryID and docIDs (i.e., the same format that is used in the qrels.csv file).  The docIDs are space separated and need to be in ranked order (the one with the highest relevance score first).  You may return up to 100 documents for each query.

The file should contain a header and have the following format:

```
queryID,docIDs
303,XIE19970211.0115 XIE20000522.0056 XIE19970513.0108 ...
307,XIE19990501.0067 XIE19961203.0196 XIE19970621.0161 ...
...
```


## FAQ

  * **Does each part need to be delivered separately?** No, you need to deliver everything at once, by the closing date.
  * **Can I use a programming language other than Python?** Yes, you may use any programming language/tool. However, you are required to submit the complete source code that produced your output.
  - **What resources can be used?**
  Everything can be used. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.
