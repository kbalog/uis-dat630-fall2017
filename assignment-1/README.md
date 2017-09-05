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
    * Search only in the `content` field.
    * Return the top 100 documents for each query in `data/queries.txt` and write the results to a `data/baseline.txt` file (see [below](#output-file-format) for the output file format).
    * The [2_Baseline_retrieval.ipynb](2_Baseline_retrieval.ipynb) notebook contains the code that you need to complete.


## Part 2 (week 36)

  - Evaluate the performance of the baseline retrieval model in terms of Mean Average Precision (MAP), Precision@10 (P@10), and Mean Reciprocal Rank (MRR).
    * The [3_Evaluation.ipynb](3_Evaluation.ipynb) notebook contains the code that you need to complete.
    * You should get around P@10=0.17, MAP=0.06, and MRR=0.31.
  - Implement the Mixture of Language Models (MLM) approach with two fields (title and content).
    * For each query, obtain the top 200 documents using the default Elasticsearch model (using the "content" field only), then re-rank these documents by computing the MLM score for each (and then return the top 100).
    * The [4_MLM_scoring.ipynb](4_MLM_scoring.ipynb) notebook contains the code that you need to complete.
    * You need to reach a **MAP score of minimum 0.07** in order to pass this assignment. (A correct implementation of the MLM method will give you that score.)


## Part 3 (week 37)

  - Find the parameter setting that yields the best performance.
    * For BM25, tune the k1 and b parameters.
    * For MLM, tune the field weights, smoothing method, and smoothing parameter.
  - Perform a query-level comparison between the baseline BM25 model (with default parameter settings) and the MLM approach (with the best parameters). Include two plots:
    * A plot showing how the performance of each query changed (delta AP scores).
    * A plot showing the distribution of queries according their AP scores were affected. Use a histogram with 7 bins according to deltaAP: [-1,-0.5), [-0.5, -0.25), [-0.25, -0.05), [-0.05, 0.05], (0.05, 0.25], (0.25, 0.5] (0.5, 1].
  - You are not given any notebooks for this part.
  - You may compete with a single ranking against other teams.
    * The competition is hosted on [Kaggle](https://inclass.kaggle.com/c/uis-dat630-2017-assignment-1)
    * The competition uses graded relevance judgments and NDCG@100 as the evaluation metric. (Documents with the highest relevance level have been shared with you in `data/qrels2.csv`; the rest of the data is withheld.)
    * You may submit max. 2 entries per day.  
    * The best performing team (each team member) will get 5 bonus points at the final exam.
    * *Details and submission link are coming soon.*


## Deliverable

  - You need to complete the [REPORT.md](REPORT.md) file in your private repository.
  - Only one report is needed per team, handed in by the team leader. Other team members only need to write the GitHub username of the team leader.
  - A team can consist of at most 3 people.
  - All code files that were used to produce the report must be included in the GitHub repository. Do not store large data files (especially your Elasticsearch index) in GitHub!
  - **Submission deadline: 18/09 10:00**. This is an absolute, immutable deadline.
  - **Important**
    * At the above deadline date, we will pull your GitHub repository. Just make sure (using the GitHub web interface) that your files have been pushed. Other than that, you don't need to submit anything (and we are not accepting submissions in any other way, like email, etc.).
    * Follow the provided report template. We are not accepting deliveries in any other format (Word, PDF, etc). If you fail to comply with the format, your assignment will not be accepted.


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

The qrels file (qrels2.csv) contains only 45 queries, i.e., for 5 queries there are no relevance assessments. Just ignore those queries that are not in qrels2.csv when computing the MAP scores.

```
queryID,docIDs
303,APW19980610.1778 APW19990525.0223 APW19990602.0039  ...
307,APW19980602.0026 APW19980603.0021 APW19980810.1038 ...
...
```


### Output file format

The output file should contain two columns: QueryId and DocumentId. For each query in `queries.txt`, up to 100 documents may be returned, in decreasing order of relevance (i.e., more relevant first).

The file should contain a header and have the following format:

```
QueryId,DocumentId
303,APW19980715.1061
303,APW19990108.0103
303,APW19990108.0283
303,XIE19970211.0115
303,XIE19980610.0069
303,XIE19991228.0201
...
307,APW19980915.0811
307,XIE19990501.0067
307,XIE19970120.0005
307,XIE19961203.0196
307,XIE19981121.0137
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
