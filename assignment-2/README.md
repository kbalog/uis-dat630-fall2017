# Assignment 2

## Task

The main task is to solve a classification problem, implementing a basic classifier, and exploring alternative techniques.

The assignment consists of three main parts.

For some parts, a skeleton of the code is provided as Jupyter notebooks. These notebooks are pushed to the private GitHub repositories. Make sure you work with the files in your private repo.


### Part A (week 38)

  * Exploring the dataset
    * The [1_Exploring_data.ipynb](1_Exploring_data.ipynb) notebook contains code as a hint.  

### Part B (week 39)

  * Build a **decision tree classifier** from the given training data set. Then, apply it on the test set and submit your predictions.
      - You need to build the decision tree classifier **from scratch**. (I.e., it is not allowed to use existing machine learning libraries or packages.)
      - You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.
      - The output (a single file with the predictions for each test instance) **must be generated automatically using the decision tree approach implemented by you**. Submitting predictions from any other source (Internet, another team, etc.) is considered cheating and will result in immediate disqualification (i.e., dismissal from the course).   
      - The predictions are also required to be submitted on [Kaggle](https://www.kaggle.com/t/42fe17fac7d54895bb0181e85b4d4d19). **The team name for the submissions must be the GitHub username of the team leader**.
      - In order to pass this assignment, you need to reach an **Accuracy of at least 0.53** on the test set.
      - The best performing team (each team member) will get 5 bonus points at the final exam (which will be 100 points in total).
      - A skeleton of a possible implementation in Python for an example dataset is made available in [this notebook](2_Decision_tree_example.ipynb).

### Part B (week 40)

  * Build a decision tree classifier (continued)

### Part C (week 41)

  * Train any **advanced classifier(s)** (different from the decision tree) and assess their performances until one is found such that it improves the decision tree from Part B.
      - You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.
      - The output (a single file with the predictions for each test instance) **must be generated automatically using the classifier of your choice**. Submitting predictions from any other source (Internet, another team, etc.) is considered cheating and will result in immediate disqualification (i.e., dismissal from the course).   
      - The predictions can optionally be submitted to another [kaggle competition](https://www.kaggle.com/t/7cd45d4a0ca44ee39c50fdad548d1a0e). **The team name for the submissions must be the GitHub username of the team leader**
      - The best performing team (each team member) will get 5 bonus points at the final exam (which will be 100 points in total).
      - In order to be eligible for the bonus, you need to reach an **Accuracy of at least 0.53874** on the test set.
      - A notebook with a possible skeleton for this part is provided [here](3_Alternative_classifiers.ipynb).


### Part C (week 42)

  * Alternative classifiers (continued)


## Deliverable

  - You need to **complete the [Report file](REPORT.md)** in your private repository.
  - The content of that Report file must be exactly the same as the starter file, excepting the replacements of the `*TODO*` parts by your data.
    - Replace the entire `*TODO*` string (not just the `TODO` substring) by your answer. E.g., if your username is johnsmith, don't write it as `*johnsmith*`.
    - In the "Additional team members" part, enter **all** the team members who are not the leader, i.e., **including yourself** if you are not the leader.
  - Only one report is needed per team, handed in by the team leader. Other team members only need to write the GitHub username of the team leader.
  - A team can consist of at most 3 people.
  - All code files that were used to produce the report must be included in the GitHub repository. Do not store large data files in GitHub!
  - **Submission deadline: 23/10 10:00**. This is an absolute, immutable deadline.


## Help

  * A **skeleton** of a possible implementation in Python for an example dataset is made available [here](2_Decision_tree_example.ipynb).
  * Since the ground truth labels are not made available, you might use some of the techniques mentioned to estimate the performance in absence of ground truth, e.g., holdout or k-fold cross validation.
  * Some **enhancement techniques** that will help you to improve accuracy:
    - Ignoring certain attributes
    - Early stopping: don't split the node further if the number of training instances is < X; make a leaf node with the majority class
    - Dealing with missing attributes: you can ignore these when building the tree and substitute missing values with the median/mode when applying the model on test data


## Data

The assignment uses the Basketball dataset. The main task is to predict, based on data from basketball matches, whether a shot was made or missed.

  - Training set: `data/basketball.train.csv`. The file contains 74,286 records in total. Each line corresponds to a record, containing information about a shot during a basketball match. The attributes are comma-separated. The last attribute is the target class label: `made` or `missed`.
  - Test set: `data/basketball.test.csv`. The file contains 37,142 records. It has the exact same format as `basketball.train.csv`, except the last column. I.e., the class labels are missing from the test file; your task is to predict these and output such predictions to a separate file.
  - There are 13 attributes, a mixture of categorical and numeric ones. See the `data/basketball.txt` file for further details on the attributes.
  - The `eval.py` script can be used for evaluation during development (if the holdout method or cross-validation is employed).
    * The `toy_data` folder contains a toy-sized ground truth set and predictions; this is only provided to allow you to try out the evaluation script. Run `python eval.py toy_data/basketball.gt.csv toy_data/basketball.pred.csv` from the assignment's root folder.


### Output files format

For each record in the test data, you need to output one line with the target label (either `made` or `missed`). The output needs to be in CSV format, including a header line:
```
Id,Target
1,made
2,missed
3,missed
4,made
5,missed
6,made
7,made
8,missed
etc.
```  
where `Id` is the line number and `Target` is the prediction (`made` or `missed`).
Mind that the evaluation is case sensitive!


## FAQ

  * **Is it possible to submit results multiple times on kaggle?**
Yes. Up to twice per day, on each competition. Only the best performing one will be considered.
  * **Is it obligatory to submit results on kaggle?**
Yes for the decision tree competition. This way you can check if you passed the Accuracy threshold.
  * **Does each part need to be delivered separately?** No, you need to deliver everything at once, by the closing date.
  * **Can I use a programming language other than Python?** Yes, you may use any programming language/tool. However, you are required to submit the complete source code that produced your output.
  * **Does everything have to be written from the ground up?**
  For the decision tree part (Part B), yes. You are allowed to use libraries for data structures and data preprocessing though.
  * **What resources can be used?**
  Everything, except machine learning libraries and ready-made decision tree implementations for Part B. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  * **Which decision tree algorithm should I implement?** It's up to you. The one we used for the exercise is [ID3](https://en.wikipedia.org/wiki/ID3_algorithm). It cannot deal with missing attributes and does not include stopping criteria or pruning; you'll have to figure out how to do that. There exist extensions to ID3, like [C4.5](https://en.wikipedia.org/wiki/C4.5_algorithm). You can look for ideas there. The recommendation is to implement ID3 and extend it as you see fit so that it works effectively on the basketball dataset.
  * **How general should the implementation be?** It does not have to be general, it should work only on the basketball dataset. You may hard-code attribute types and even splitting conditions for continuous attributes. You may also hard-code which attributes should be used and which are to be ignored. However, when running the code, it should produce an output file from the two input files (training and test data) without any human intervention.
  * **Should each member of the team write a separate report?** No, there is a single report from the team.
  * **Is it possible to get a deadline extension?**
      No. Don't even ask.
  * **Can I take the exam if I fail to complete this assignment?**
      No. So you better take it seriously.
