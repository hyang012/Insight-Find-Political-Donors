# Table of Contents
1. Introduction
2. Description
3. Dependencies

# Introduction
This repo contains the solution to the Insight's Coding Challenge Project (Feb 2018) - [Donation Analytics](https://github.com/InsightDataScience/donation-analytics).

# Description
In this project, there are four python files in the src folder - `donation-analytics.py` is the script that contains the main program, each of `record.py` and `analytic_result.py` defines a class that is used in the main program and finally `data_utils.py` contains functions that related to setting up input data files. 

The `donation-analytics.py` takes in two files in the input folder:
1. `itcont.txt` - a file of which each line represents a record of political donation.
2. `percentile.txt` - a file that has a line of a value from 1 to 100 indicating the percentile that the program needs to calculate.

From the two input files, for each recipient, zip code and calendar year, the program prcoesses each donation record, identifies the donations that are from repeat donors and calculates the following four fields:
1. total dollars received
2. total number of contributions received
3. donation amount in a given percentile
4. running percentile of contributions received from repeat donors

For each line of the input file, the program prints a line with the recipient id, zip code, calendar year and the four fields to a file `repeat_donors.txt`, which is in the output folder.

# Dependencies
The program uses the following three dependencies:
1. `bisect`
2. `datetime`
3. `sys`
