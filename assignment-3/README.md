# Assignment 3

**Updates (most recent first):**
  - The [Kaggle competition](https://www.kaggle.com/t/408f3cbd43e0494da0426b2fb441bab2) has been launched. The minimum NDCG@20 score to reach for passing this assignment has been (very generously) set to 0.1.
  - Caching has been added to the API. Getting search results and termvectors should be much faster from now on.
  - [Slides](https://speakerdeck.com/kbalog/2017-learning-to-rank) have been updated with specific feature suggestions. The notebook for Part 3 is [available here.](3_LTR.ipynb).
  - LM scoring code has been shared in the [LM_scoring.ipynb](LM_scoring.ipynb) notebook.
  - Two new API requests have been added: (1) `exists` for checking if a given document exists in the index (instead of using `termvectors` for that) and (2) `analyze` for tokenizing the query for custom retrieval.
  - It's enough to output top-20 results (was 100 before).
  - The indices are final. We posted the NDCG@10 scores that you should get for the baseline methods.

The task is to implement methods for web search and evaluate them using a standard test collection.

The assignment consists of three main parts.

For each part a skeleton of the code are provided as Jupyter notebooks. These notebooks are pushed to the private GitHub repositories. Make sure you work with the files in your private repo.


## Part 1 (week 43)

  - Perform baseline retrieval using Elasticsearch and BM25 (i.e., the default model).
  - An Elasticsearch index is already created (that is, we already indexed the document collection for you). You can access it via an API; see [below](#search-api).
  - Search separately in two fields: `title` and `content` and report on the performance.
    * Return the top 20 documents for each query in `data/queries.txt` and write the results to a `data/baseline_title.txt` and `data/baseline_content.txt` files (see [below](#output-file-format) for the output file format).
    * Evaluate the results against the ground truth (in `data/qrels.csv`) in terms of NDCG@10 and NDCG@20.
       - You should get an NDCG@10 around 0.14 for the content field and 0.12 for the title field.
       - In the NDCG computations, use gain=0 for documents with relevance < 0.
  * The [1_Baseline.ipynb](1_Baseline.ipynb) notebook contains sample code for talking to the API.


## Part 2 (week 44)

  - Implement a learning-to-rank method with the following minimum requirements:
      - Consider document-query matching in minimum 3 fields (title, content and anchors) and at least two different retrieval models (e.g., BM25 and LM). That is, 6 document-query features minimum.
      - The code for language modeling scoring (if you prefer our implementation over yours from Assignment 1) is made available in [LM_scoring.ipynb](LM_scoring.ipynb).
  - Perform baseline (BM25) retrieval on a separate anchor text index.
      - The anchor text index (called `clueweb12b_anchors`) can be accessed the same way as the regular document index. See [below](#search-api).
      - Note that the anchor text index covers the entire ClueWeb collection, not just the Category B subset. I.e., you need to ignore documents that are not present in the regular index.
      - The anchor text index should give an NDCG@10 score of 0.105
  - Test your model using 5-fold cross-validation on the given training data (queries and relevance judgments, i.e., `data/queries.txt` and `data/qrels.csv`).
  - No notebook is provided for this part of the assignment.
      - Use the [code from Practicum 9](https://github.com/kbalog/uis-dat630-fall2017/tree/master/practicum/practicum-9/solutions) as your starting point.


## Part 3 (week 45)

  - Design and implement additional features to maximize retrieval performance.
      - Add minimum 2 query and minimum 2 document features (see lecture slides for suggestions).
      - PageRank scores for the ClueWeb collection are [available here](http://www.lemurproject.org/clueweb12/PageRank.php). Specifically, since the work with the "Category B" subset, the files under the "ClueWeb12-B13 PageRank" heading are to be used.
      - Note: you *don't have to* use PageRank as a feature. If you want, you can take PageRank scores from one of these files (and you need to figure out the file format yourself; but really, it is not that complicated).
  - Learn a model on the given training data (i.e., using `data/queries.txt` and `data/qrels.csv`) and apply that model on the set of "unseen" queries in `data/queries2.txt`.
  - A notebook is provided for Part 3 that contains the main logic and only needs the additional features to be implemented.
      - The notebook is called [3_LTR.ipynb](3_LTR.ipynb). *It'll soon be pushed to the private repos. For now, you can get it from [this link](3_LTR.ipynb).*
  - You need to submit the generated ranking on Kaggle and **reach a minimum NDCG@20 score of 0.1**.
      - The Kaggle competition is available here: [https://www.kaggle.com/t/408f3cbd43e0494da0426b2fb441bab2](https://www.kaggle.com/t/408f3cbd43e0494da0426b2fb441bab2)
  - Additionally, the best performing team will be awarded with 5 bonus points (each member).



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
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/clueweb12-0209wb-65-17913/_termvectors?term_statistics=true`
    - NOTE: do not use the termvectors request to check if a document exists in the index. Use the exists endpoint instead (see next).
  * **Exists**: `/<indexname>/<docid>/_exists`
    - Returns whether the given document ID exists in that index using [es.exists()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.exists)
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/clueweb12-1700tw-22-12689/_exists`
  * **Analyze**: `/<indexname>/_analyze`
    - Returns the analyzed version of the input text using [es.indices.analyze()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.client.IndicesClient.analyze)
    - This endpoint is needed when using another retrieval method for scoring the query (e.g., LM). Instead of just splitting by spaces, use this request for tokenizing the query text.
    - Parameters:
        - `text` (mandatory): text to be analyzed
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/_analyze?text=World%27s+biggest+dog`


The API may be extended over time with additional functionality, should the need arise.  If you have specific requests, do let us know.

## FAQ for Assignment 3

  * **Are the indices final?** Yes.
  * **Can we get a deadline extension because the indexing was delayed?** No. We compensated for the indexing delays by reducing the amount of deliverables (compared to what was planned originally for this assignment).
  * **How to deal with junk documents with relevance=-2?** When computing NDCG, use gain 0 for those results.  On the other hand, when training the model, use -2 as the target value (so that your model can learn to rank those results real low).
  * **Should we use binary target labels (i.e., target=1 if rel>0 and target=0 if rel<=0)?** No. Use the relevance labels directly as target values. We are treating it as a regression problem, not as a binary classification task.
  * **Is it possible to query the API using different similarity methods?** No. As the index would need to be closed and re-opened after each such change, it would reduce the throughput of the API too much.
  * **Will it not be a lot of work for us then to implement another retrieval method?** You should have the LM implementation from Assignment 1 that you can reuse.  We also made our LM implementation available [here](LM_scoring.ipynb). You may also choose a simpler similarity function, e.g., TF-IDF or even just TF or IDF.
  * **I'm getting a lower NDCG score for the baselines than what I'm supposed to.** Make sure you treat relevance=-2 as relevance=0 when computing NDCG.
  * **Do we need to use the PageRank scores from that link?** No. It's up to you. If you want, you can use them. What matters is that you implement at least 2 document features.
  * **How to check if a given document that we retrieve from the anchors text index exists in ClueWeb Category B?** A separate `exists` request has been introduced for that. Do not use `termvectors`, as that is too slow. Only use `termvectors` when computing the retrieval scores for a given document.
  * **How many documents to retrieve for the anchors-only baseline?** You need to figure it out. For some queries, you might need to retrieve up to 1000 or 2000 docs to find 20 that exist in the `clueweb12b` index. For other queries, it could be much less.
  * **Running the experiments takes a lot of time.** If you request all the data from the API each time you make a change or try to add a new feature, then yes, it'll take a very long time. You should compute individual features only once and store these somewhere (e.g., text or json files).


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
