# Assignment 2

## Task

The main task is to solve a classification problem, implementing a basic classifier, and exploring alternative techniques.

The assignment consists of three main parts.

For some parts, a skeleton of the code is provided as Jupyter notebooks. These notebooks are pushed to the private GitHub repositories. Make sure you work with the files in your private repo.


### Part A (week 38)

  * Exploring the dataset
    * The [1_Exploring_data.ipynb](1_Exploring_data.ipynb) notebook contains code as a hint.  

### Part B (week 39)

  * Implementing a Decision Tree

### Part B (week 40)

  * Implementing a Decision Tree (continued)

### Part C (week 41)

  * Alternative classifiers  

### Part C (week 42)

  * Alternative classifiers (continued)


## Deliverable

  - You need to complete a Report file in your private repository.
  - Only one report is needed per team, handed in by the team leader. Other team members only need to write the GitHub username of the team leader.
  - A team can consist of at most 3 people.
  - All code files that were used to produce the report must be included in the GitHub repository. Do not store large data files in GitHub!
  - **Submission deadline: 23/10 10:00**. This is an absolute, immutable deadline.


## Data

The assignment uses the Basketball dataset. The main task is to predict, based on data from basketball matches, whether a shot was made or missed.

  - Training set: `data/basketball.train.csv`. The file contains 74,286 records in total. Each line corresponds to a record, containing information about a shot during a basketball match. The attributes are comma-separated. The last attribute is the target class label: `made` or `missed`.
  - Test set: `data/basketball.test.csv`. The file contains 37,142 records. It has the exact same format as `basketball.train.csv`, except the last column. I.e., the class labels are missing from the test file; your task is to predict these and output such predictions to a separate file.
  - There are 13 attributes, a mixture of categorical and numeric ones. See the `data/basketball.txt` file for further details on the attributes.
  - The `eval.py` script can be used for evaluation during development (if the holdout method or cross-validation is employed).
    * The `toy_data` folder contains a toy-sized ground truth set and predictions; this is only provided to allow you to try out the evaluation script. Run `python eval.py toy_data/basketball.gt.csv toy_data/basketball.pred.csv` from the assignment's root folder.


### Output file format

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

  * **Does each part need to be delivered separately?** No, you need to deliver everything at once, by the closing date.
  * **Can I use a programming language other than Python?** Yes, you may use any programming language/tool. However, you are required to submit the complete source code that produced your output.
  * **Does everything have to be written from the ground up?**
  For the decision tree part (Part B), yes. You are allowed to use libraries for data structures and data preprocessing though.
  * **What resources can be used?**
  Everything, except machine learning libraries and ready-made decision tree implementations for Part B. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  * **Should each member of the team write a separate report?** No, there is a single report from the team.
  * **Is it possible to get a deadline extension?**
      No. Don't even ask.
  * **Can I take the exam if I fail to complete this assignment?**
      No. So you better take it seriously.
