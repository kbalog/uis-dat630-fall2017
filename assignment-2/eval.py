"""
Evaluation script for Python 3.

Run:
    python eval.py file_ground_truth file_predictions

Where:
    - file_ground_truth is a csv file with a ground truth
    - file_predictions is a csv file with the predictions

The files should contain a header and have the following format:
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
where Id is the line number and Target is the prediction (made or missed).

@author: Krisztian Balog (krisztian.balog@uis.no)
@author: Dario Garigliotti (dario.garigliotti@uis.no)
"""

from __future__ import division

import sys
import csv


def load_file(filename):
    """Load a csv file into a dictionary."""
    data = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for row in csvreader:
            if row['Target'] not in ["missed", "made"]:
                print("Error: Unrecognized or missing class label '{}' in file '{}'".format(row['Target'], filename))
                return -1

            data[row['Id']] = row['Target']
    return data


def eval(file_gt, file_predictions):
    """Perform evaluation."""

    # Load ground truth file and predictions file
    data_gt = load_file(file_gt)
    data_pred = load_file(file_predictions)

    correct = 0
    incorrect = 0
    total = len(data_gt)

    if total == 0:
        print("Error: Empty ground truth file")
        return -1

    for id, label in data_gt.items():
        if id not in data_pred:
            print("Error: Missing prediction for Id=" + id)
            return -1

        if data_pred[id] == label:
            correct += 1
        else:
            incorrect += 1

    acc, err = str(correct / total)[:6], str(incorrect / total)[:6]  # max 3 digits
    print("Accuracy:   ", acc)
    print("Error rate: ", err)

    return acc, err


def print_usage():
    print("Usage: python eval.py file_ground_truth file_predictions")
    sys.exit()


def main(argv):
    if len(argv) < 2:
        print_usage()

    eval(argv[0], argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])
