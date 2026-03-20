# Health Monitoring Data Processing

You are a junior data engineer at a Taiwan-based wearable health-tech firm called Seng-Links. Your company has just discovered that the raw heart-rate exports from prototype devices are inconsistent. Some files contains malformed records, impossible values, or missing entries. Before the machine learning team can study usage and identify sleep & exercise patterns, the data engineering team must build a batch-processing pipeline that reads raw files cleans records, computes quality checks, and calculates descriptive statistics for later analysis.

Your company has provided you a folder named "data/", which contains 4 files of heart-rate samples from one 30 year old participant. The participants device records heart rate every 5 minutes. Your task is to write a Python program that:
1. Reads raw files from the `data/` folder.
2. Cleans the records by ignoring invalid or missing values.
3. Computes and prints descriptive statistics for each file.

## Instructions

There are two Python files which you will modify in this repository to complete this project:
* main.py
* writeup.md

Once you've completed the coding portion of this project in the `main.py` file and ensured that your output is correct, you will then provide a writeup in the file `writeup.md`, where you will answer analytical questions on the data you've analyzed.

**main.py**

You can run this module by typing and executing the following command in your terminal: 

```
python main.py
```

This module serves as the main data pipeline for your project. It integrates the functions you implemented to read the raw data files (using file I/O), compute descriptive statistics (using for-loops), and generate outputs for your analysis. 

This module contains the following functions:

* `clean_heartrate_data`
* `average`
* `median`
* `range`
* `rolling_avg` (Challenge function)
* `run`

You will implement each function, and subsequently call these functions within the `run` function to implement your full data pipeline. Some helpful hints for each function are listed below:

`run`: This function takes a string containing the relative filepath as input. We will use this string to read in our data as a list using File I/O. We recommend starting with this function when beginning your project. Note that you can complete this function even if the `clean_heartrate_data`, `average`, `median`, and `range` are not yet completed. 

`clean_heartrate_data`: This function takes in a list of strings and filters out all strings that include non-digit characters. Remove the new-line character (`\n`) before performing this digit check! After validating that a string is a valid digit, you will convert this element into an integer and append it to a new list, which will be returned when your function ends. You will also return a variable that represents the number of rows you've skipped due to erroneous values.

`average`, `median`, `range`: These three functions calculate various descriptive statistics on your cleaned data. For example, in the `average` function, you will calculate the average heart value of all input data. 

As these functions will only be called **after** you've cleaned and removed outliers, you can expect your list of data to be integers. Be sure to round all floating-point values to 2 decimal points!

**NOTE**: You must implement all statistical formulas using base Python, and you cannot use modules that calculate these metrics for you (e.g., `stats.avg()`). Furthermore, you should use a for-loop for both average and maximum to calculate the average and maximum, respectively.

**writeup.md**

This file contains 3 analytical questions you will answer based on the metrics your code generates.

## Submission 

The due date for this project is `03/20`.

To begin work on this project, you will create a repository in your GitHub and copy all these template files into your repo.

Be sure to test as you code as you develop in order to verify that your functions are working correctly. 

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

