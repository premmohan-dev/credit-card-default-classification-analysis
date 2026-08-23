# Credit Card Default Classification Analysis

## Overview

This analysis explores factors associated with credit card default and uses a decision tree model to predict whether a customer will default on their next payment.

## Objectives

- Analyze customer characteristics associated with credit card default.
- Examine how default rates vary across customer groups.
- Explore relationships between credit limits, repayment history, and default status.
- Identify factors associated with default payment behavior.
- Build a decision tree classification model to predict whether a customer will default on their next payment.

## Dataset

This analysis uses the Default of Credit Card Clients dataset from the UCI Machine Learning Repository. The dataset was created by I-Cheng Yeh and was donated to the UCI Machine Learning Repository on January 25, 2016.

The dataset contains information for 30,000 credit card customers in Taiwan and includes demographic characteristics, credit limits, repayment history, bill statements, payment amounts, and default status.

The target variable is whether a customer defaulted on their next credit card payment.

Key variables include:

- Credit Limit (LIMIT_BAL)
- Sex
- Education Level
- Marital Status
- Age
- Repayment History (PAY_0 through PAY_6)
- Bill Statement Amounts (BILL_AMT1 through BILL_AMT6)
- Payment Amounts (PAY_AMT1 through PAY_AMT6)
- Default Payment Next Month (Target Variable)

Dataset License: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Research Questions

### 1) How do default rates vary across customer demographic groups?

Education levels in the dataset are coded as:

- 1 = Graduate School
- 2 = University
- 3 = High School
- 4+ = Others

### Key Findings

Default rates varied across the major education groups. Customers with a high school education had the highest rate at 25.16%. University graduates followed at 23.73%, while graduate school attendees had the lowest at 19.23%. These results suggest that customers with higher levels of education were generally less likely to default.

### 2) How do credit limits differ between customers who default and customers who do not?

### 3) How does repayment history relate to default status?

### 4) Can a decision tree model predict whether a customer will default on their next payment?

## Methods

- Data cleaning and preparation in Microsoft Excel
- SQL analysis in Microsoft Access
- Exploratory data analysis in Python
- Data visualization using Python libraries
- Decision tree classification modeling
- Interpretation of model performance and classification results

## Tools and Technologies

- Microsoft Excel
- Microsoft Access
- SQL
- Python
- Pandas
- Matplotlib
- Scikit-learn
