---
created: 2023-10-25T11:11:28 (UTC -07:00)
tags: []
source: https://csus.instructure.com/courses/111137/assignments/1911584
author:
---

# Linear Regression Project & Classification Tree Homework

Dear Students,

## (a) Regression - Using any of the data in previous assignment

Intelligently choose any one of the data sets you used in your previous
assignment and apply Linear Regression on the data. You had created Training
and Test sets in the previous assignment by partitioning (splitting) your
original data set. Apply Linear Regression on the Training set and test with
the Test set.

If a previous dataset is not suitable for regression, you may use a different
dataset of your own choice or add a new X or Y column of numerical data type as
needed to your previous dataset creatively!

Use both Simple Linear Regression model and Multiple Regression Model to fit
your data. For the simple linear regression model, select any two variables as
**x** and **y**. Use the Test data to predict **y** for new **x** values.
Make sure your Test data contains **x** values both within the Training range
of **x** and outside the Training range of **x** (so you can test both
interpolation and extrapolation).

Since you have two pairs of partitioned sets, do regression analysis separately
on both pairs. Plot the data (and the line). Save the picture.
Record your observations in a report.

Regression models may behave badly if correlations are weak, or outliers are
not analyzed and processed upfront. Also, if data is not standardized or
normalized especially in the case of regularization. Understand the importance
of standardizing or normalizing the data before performing your experiments.
For those who like to dive one step deeper, you may refer to these two articles
on feature scaling for regularization.

[Wikipedia - Feature scaling](https://en.wikipedia.org/wiki/Feature_scaling)

[scikit-learn: 6.3. Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)

## (b) Regression and Classification using a new data set provided in file

Please use the following excel file from CANVAS:

Files --> LabHelp --> Labs/data/Linear_Regression_data/Admission_Predict_Ver1.1_small_data_set_for_Linear_Regression.xlx

**Now a CSV**: [Admission Predict Ver1.1 small data set for Linear Regression](admission_predict_ver1.1_small_data_set_for_linear_regression.csv)

There is also a description pdf file in the same directory.
Also manually inspect and study the data. Make any random observations about the
data. Now, do the same operations in (a) on this smaller data set. Use only one
pair of training and test partitions of the original data.

Record your observations in a report. Plot the data (and the line).
Save the picture.

Regression models may behave badly if correlations are weak, or outliers are
not analyzed and processed upfront. Also, if data is not standardized or
normalized especially in the case of regularization. Understand the importance
of standardizing or normalizing the data before performing your experiments.
For those who like to dive one step deeper, you may refer to these two articles
on feature scaling for regularization.

[Feature scaling - Wikipedia Links to an external site.](https://en.wikipedia.org/wiki/Feature_scaling)

[6.3. Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)

## Classification

Discretize the last column "Chance of Admit" into three classes and create a
classification tree with training data. Test the tree with test data and
evaluate the results in Python.

Describe a few rules (3 to 5 valuable rules are sufficient).
Which rules do you think are the most valuable?

You may combine both the reports into one and submit the
Jupyter notebook file and the report.

## (c) Classification Tree Homework

View the Files --> Homework sheets --> [Entropy_ID3_Exercise.pdf](Entropy_ID3_Exercise.pdf)

and workout the exercise.

### (i) Create the solution

### (ii) Understand what impact may happen to your created tree, if you later add

a new missing attribute after creating the tree? You may add any new attribute,
for example, "pattern of shirt". The values may be "checked", "striped", and
one or two more. Be creative, add your own new favorite attribute or keep
"pattern of shirt". The class column remains the same.

- What are some of the different possible changes you may expect to see on the
  classification decision tree you just created?
  - Add this analysis to your solution document and submit.
- What if a data scientist provided his or her results with high confidence,
  by missing this attribute altogether?
- What if his or her results are used for
  decision making on how many million more shirts to produce for the next year?
- Do you think the data scientist surprises and makes an impact on the manager
  and CEO in case he or she discovers the new attribute and it's influence in
  getting more reliable results valuable to the company?

## Assignment 2 - Grading Percentage Breakdown

All of (a), (b) and (c) are team projects. Only one member submit.

In your submission comment state the name of your team.
Provide details of each team member's contribution.
Please submit a PDF file only for your report.

(a) --> 30%

(b) ---> 20% regression 20 % classification

(c) ---> 30%

| Criteria                                                        | Pts               |
| --------------------------------------------------------------- | ----------------- |
| Part A - Linear and multilinear regression                      | 30 pts            |
| Part B (1) - Linear and multilinear regression on given dataset | 20 pts            |
| Part B (2) - Classification on given dataset                    | 20 pts            |
| Part C (2) - ID3 entropy problem                                | 25 pts            |
| Part C (3) - Answer questions in Part C of assignment           | 5 pts             |
|                                                                 | Total Points: 100 |

## Additional Resources

If you are inclined, here are links to additional reading material.
Open the links and read only the first paragraph to get an idea what
the article is about and see if you want to read further for any kind of
deeper understanding. Also you may refer to articles in the Linear Regression
section under Modules.

1. Coding
   - [Real Python - Linear Regression in Python](https://realpython.com/linear-regression-in-python/)
2. Fitting and plotting
   - [Stack Overflow - How to fit and plot a linear regression line in python?](https://stackoverflow.com/questions/50280694/how-to-fit-and-plot-a-linear-regression-line-in-python)
   - [StackExchange - Data Science - Plotting multivariate linear regression](https://datascience.stackexchange.com/questions/27740/plotting-multivariate-linear-regression)
3. Preprocessing (normalizing and such)
   - [scikit-learn: 6.3. Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)
4. Lasso and ridge regression (using new loss functions)
   - [5 Questions which can teach you Multiple Regression (with R and Python)](https://www.analyticsvidhya.com/blog/2015/10/regression-python-beginners/?utm_source=blog&utm_medium=RideandLassoRegressionarticle)
   - [Ridge and Lasso Regression in Python | Complete Tutorial (Updated 2023)](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)
5. Types of variables
   - [Types of Variable](https://statistics.laerd.com/statistical-guides/types-of-variable.php)
6. Classification trees
   - [Decision Tree Classification in Python Tutorial](https://www.datacamp.com/community/tutorials/decision-tree-classification-python)

cheers,

:)

Jagan
