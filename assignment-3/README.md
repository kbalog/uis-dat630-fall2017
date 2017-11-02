# Assignment 3

The task is to implement methods for web search and evaluate them using a standard test collection.

The assignment consists of three main parts.

For each part a skeleton of the code are provided as Jupyter notebooks. These notebooks are pushed to the private GitHub repositories. Make sure you work with the files in your private repo.


## Part 1 (week 43)

  - Perform baseline retrieval using Elasticsearch and BM25 (i.e., the default model).
  - An Elasticsearch index is already created (that is, we already indexed the document collection for you). You can access it via an API; see [below](#search-api).
  - Search separately in two fields: `title` and `content` and report on the performance.
    * Return the top 100 documents for each query in `data/queries.txt` and write the results to a `data/baseline_title.txt` and `data/baseline_content.txt` files (see [below](#output-file-format) for the output file format).
    * Evaluate the results against the ground truth (in `data/qrels.csv`) in terms of NDCG@10 and NDCG@20.
  * The [1_Baseline.ipynb](1_Baseline.ipynb) notebook contains sample code for talking to the API.


## Part 2 (week 44)

  - Implement a learning-to-rank method with the following minimum requirements:
      - Consider document-query matching in minimum 3 fields (title, content and anchors) and at least two different retrieval models (e.g., BM25 and LM). That is, 6 document-query features minimum.
  - Perform baseline (BM25) retrieval on a separate anchor text index.
      - The anchor text index (called `clueweb12b_anchors`) can be accessed the same way as the regular document index. See [below](#search-api).
      - Note that the anchor text index covers the entire ClueWeb collection, not just the Category B subset. I.e., you need to ignore documents that are not present in the regular index.
  - Test your model using 5-fold cross-validation on the given training data (queries and relevance judments, i.e., `data/queries.txt` and `data/qrels.csv`).
  - No notebook is provided for this part of the assignment.
      - Use the [code from Practicum 9](https://github.com/kbalog/uis-dat630-fall2017/tree/master/practicum/practicum-9/solutions) as your starting point.


## Part 3 (week 45)

  - Design and implement additional features to maximize retrieval performance.
      - Add minimum 2 query and minimum 2 document features.
  - Learn a model on the given training data (i.e., using `data/queries.txt` and `data/qrels.csv`) and apply that model on the set of "unseen" queries in `data/queries2.txt`.
  - You need to submit the generated ranking on Kaggle and reach a minimum NDCG score.
  - Additionally, the best performing team will be awarded with bonus points.
  - *More details will follow*


## Deliverable

  - You need to complete the [REPORT.md](REPORT.md) file in your private repository.
  - Only one report is needed per team, handed in by the team leader. Other team members only need to write the GitHub username of the team leader.
  - A team can consist of at most 3 people.
  - All code files that were used to produce the report must be included in the GitHub repository. Do not store large data files on GitHub!
  - **Submission deadline: 13/11 10:00**. This is an absolute, immutable deadline.
  - **Important**
    * At the above deadline date, we will pull your GitHub repository. Just make sure (using the GitHub web interface) that your files have been pushed. Other than that, you don't need to submit anything (and we are not accepting submissions in any other way, like email, etc.).
    * Follow the provided report template. We are not accepting deliveries in any other format (Word, PDF, etc). If you fail to comply with the format, your assignment will not be accepted.


## Data

### Document collection

The document collection is the [ClueWeb12](http://lemurproject.org/clueweb12/) dataset, specifically the "Category B" subset of it.  It consists of around 50 million pages.  

  * An Elasticsearch index of the documents (web pages) `clueweb12b` is provided with `title`, `url`, and `content` fields.  Content comprises only the visible text from the HTML source.
  * The anchor texts are stored in a separate index called `clueweb12b_anchors`.  Mind that this index contains the anchor texts for all ClueWeb documents, not only documents from the Category B subset. It means that documents that are present in this index, but not in the `clueweb12b` index, should be ignored.


### Queries

The [queries.txt](data/queries.txt) file contains 50 queries in total.  Each line starts with a 3-digit queryID, followed by the query string.  E.g.,

```
151 403b
152 angular cheilitis
...
```

You are provided with the relevance judgments for these queries (see below).

The [queries2.txt](data/queries2.txt) file contains additional 50 queries. These are "unseen" queries, for which you'll have to generate document rankings, but you don't get to see the corresponding relevance judgments.


### Relevance judgments

The [qrels.csv](data/qrels.csv) file contains the relevance judgments for the queries in `data/queries.txt`. Each line contains the relevance label for a query-document pair.  Relevance ranges from -2 to 4, where -2 is used for junk/spam pages and 0..4 is used to indicate the degree of relevance from non-relevant to highly relevant.

Note that this file may contain document IDs that are not present in the index. Just ignore those.

```
QueryId,DocumentId,Relevance
201,clueweb12-0000tw-05-12114,1
201,clueweb12-0000wb-30-01951,0
201,clueweb12-0000wb-60-01497,1
...
```


### Output file format

The output file should contain two columns: QueryId and DocumentId. For each query, up to 100 documents may be returned, in decreasing order of relevance (i.e., more relevant first).

The file should contain a header and have the following format:

```
QueryId,DocumentId
201,clueweb12-0108wb-86-18203
201,clueweb12-0209wb-62-29857
201,clueweb12-0300tw-49-08295
...
202,clueweb12-0001wb-80-19541
202,clueweb12-0001wb-85-15380
202,clueweb12-0001wb-99-29092
...
```


## Search API

A distributed index of the ClueWeb12B collection is built using the Amazon Elasticsearch Service on AWS (using Elasticsearch version 5.5).

There is a simple API that is made for requesting data from this index (this is essentially to make the index *read-only*, preventing anyone to accidentally make any unwanted modifications).
The API is available at `http://gustav1.ux.uis.no:5002`.
The index is called `clueweb12b`, with fields `url`, `title`, and `content`.

The API source code is [available here](api.py). Note that you don't need to run it, this is only provided for transparency (so that you can see what exactly is happening in there).

Currently, the following functionality is supported.

  * **Search**: `/<indexname>/_search`
    - Execute a search query using [es.search()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.search) and returns the search hits
    - Parameters:
        - `q` (mandatory): query
        - `df` (mandatory): field to search in
        - `size` (optional): number of hits to return (default: 10)
    - Examples:
        - searching in the title field of the document index `http://gustav1.ux.uis.no:5002/clueweb12b/_search?q=united+states&df=title&size=20`
        - searching in the anchor text index: `http://gustav1.ux.uis.no:5002/clueweb12b_anchors/_search?q=united+states&df=anchors&size=20`
  * **Termvectors**: `/<indexname>/<docid>/_termvectors`
    - Returns information and statistics on terms in the fields of a particular document using [es.termvectors()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.termvectors)
    - Parameters:
        - `term_statistics` (optional): set true to return term statistics (default is false)
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/clueweb12-0000tw-07-01629/_termvectors?term_statistics=true`

The API may be extended over time with additional functionality, should the need arise.  If you have specific requests, do let us know.

## FAQ for Assignment 3

  * **Are the indices final?** Yes.
  * **Can we get a deadline extension because the indexing was delayed?** No. We compensated for the indexing delays by reducing the amount of deliverables (compared to what was planned originally for this assignment).
  * **How to deal with junk (relevance=-2) documents when computing NDCG?** The gain for that document is -2, i.e., you get a penalty for returning a junk result.
  * **Should we use binary target labels (i.e., target=1 if rel>0 and target=0 if rel<=0)?** No. Use the relevance labels directly as target values. We are treating it as a regression problem, not as a binary classification task.


## General FAQ
  * **Does each part need to be delivered separately?** No, you need to deliver everything at once, by the closing date.
  * **Can I use a programming language other than Python?** Yes, you may use any programming language/tool. However, you are required to submit the complete source code that produced your output.
  - **What resources can be used?**
  Everything can be used. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.
