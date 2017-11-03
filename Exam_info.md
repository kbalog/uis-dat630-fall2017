# Exam Information

*DRAFT version, subject to changes!*

  * Exam will be **bring-your-own-device**.
  * **Date: 04/12**

## Rules

### Can be used

  * Calculator
  * All written (printed) material
  * All **offline** resources available on your device, including
     - Any files you previously downloaded (PDFs, slides, MS Excel files, python code, etc.)
     - Programs that are installed on your PC
  * **No online resources**
  * *Note: Slides will be made available in PDF format for download*

### Grading

  * Multiple choice questions:
    - 2 or 3 points if correct
    - 0 if unanswered
    - -1 if incorrectly answered
  * Total points: 100
  * Grading
    - 0-39	F
    - 40-49	E
    - 50-59	D
    - 60-79	C
    - 80-89	B
    - 90+	A

## Topics

Motto: "everything from the lectures and practicums"

### Data Mining

  * Intro: challenges, workflow, tasks
  * Types of attributes; attributes properties, transformations
  * Types of data sets
  * Data quality problems and issues
  * Data preprocessing
  * Proximity measures
    - Similarity vs. distance
    - Normalization (min-max)
    - Similarity/distance for single attributes (depending on attr. type)
    - Similarity/distance between data objects
        * Numerical attributes: Eucledian, Minkowski, Cosine
        * Binary attributes: Simple Matching Coefficient, Jaccard
  * Summary statistics
    - Frequency, mode, percentiles, mean, median, range, variance, std. deviation
    - Absolute Average Deviation, Median Absolute Deviation, Interquartile Range
  * Visualization
  * OLAP and Multidimensional Data Analysis
  * Classification
    - Intro: motivation, task, approach, objectives
    - Decision trees
        * Basics: node types, model application
        * Tree induction, Hunt's algorithm, how to split, impurity measures, gain, stopping criteria, expressivity
    - Rule-based classifiers
        * Rule sets and their properties, coverage and accuracy, rule ordering, creating a rule-based classifier from a decision tree, simplification
    - Nearest neighbors
    - Naive Bayes
        * Bayes Theorem
        * Estimation of conditional probabilities for different attribute types, smoothing
    - Main ideas behind Ensemble Methods
    - Multiclass classification
        * One-against-rest and one-against-one approaches
    - Underfitting and overfitting
    - Class imbalance
    - Evaluation
        * Confusion matrix
        * Type I and II Errors
        * Evaluation measures (accuracy, precision, recall, F1, true/false positive/negative rate)
  * Supervised vs. unsupervised learning
  * Clustering
    - Motivations
    - Types of clusterings and of clusters
    - K-means clustering (basic and bisecting)
        * Criteria and issues for the algorithm' steps
        * Issues, limitations
    - Hierarchical agglomerative clustering
  * Locality sensitive hashing
  * Frequent itemsets and association rule mining
    - A-Priori, SON, PCY algorithms


### Information Retrieval

  * Search engine architecture
  * Indexing
    - Inverted index with term frequency or with position information
  * Text preprocessing
    - Tokenization, stopword removal, stemming
  * Term vectors, TFIDF term weighting
  * Retrieval models
    - Boolean retrieval
    - Vector space model
    - BM25
    - Language models
       * Different smoothing methods (Jelinek-Mercer, Dirichlet)
    - Fielded retrieval models (BM25F, Mixture of Language Models)
  * Evaluation
    - Precision, recall, (mean) average precision, (mean) reciprocal rank, NDCG
  * Web retrieval
    - Web crawling
    - Anchor text
    - Pagerank
    - SEO
  * Learning-to-rank
    - Difference between pointwise, pairwise, listwise methods
    - Types of features (query, document, query-document)
  * Semantic search
    - Knowledge bases, RDF, DBpedia
    - Entity retrieval
    - Entity linking
