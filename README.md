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

<img width="989" height="590" alt="RQ1_DefaultRates" src="https://github.com/user-attachments/assets/402dcc28-1071-4f07-b2f8-db77854f2717" />

### Key Findings

Default rates varied across the major education groups. Customers with a high school education had the highest rate at 25.16%. University graduates followed at 23.73%, while graduate school attendees had the lowest at 19.23%. These results suggest that customers with higher levels of education were generally less likely to default.

### 2) How do credit limits differ between customers who default and customers who do not?

### Key Findings

Credit limits differed noticeably between customers who defaulted and those who did not. Customers who did not default had an average credit limit of 178,099.73, compared to 130,109.66 for customers who defaulted. Higher credit limits were generally associated with lower default rates in the dataset.

### 3) How does repayment history relate to default status?

Repayment status codes are defined as:

- -2 = No consumption
- -1 = Paid in full
- 0 = Use of revolving credit
- 1 = Payment delay for one month
- 2 = Payment delay for two months
- 3 = Payment delay for three months
- 4+ = Payment delays of four months or longer

### Key Findings

Default rates varied substantially across repayment status groups. Customers with no recent repayment issues generally reported default rates between 12.81% and 16.78%. Customers with a one-month payment delay had a default rate of 33.95%, while those with a two-month delay exceeded 69%. Overall, customers with recent repayment delays were much more likely to default on their next payment.

### 4) Can a decision tree model predict whether a customer will default on their next payment?

<img width="1569" height="799" alt="RQ4_DecisionTree" src="https://github.com/user-attachments/assets/6638d8a3-667a-4adc-8b48-af559d6e40ea" />

### Key Findings

The decision tree model achieved an accuracy of 81.92% when predicting whether a customer would default on their next payment. The model correctly classified 6,685 non-defaulting customers and 688 defaulting customers in the test dataset. Repayment history variables such as PAY_0, PAY_2, and PAY_3 appeared near the top of the decision tree, indicating that recent repayment behavior was among the most important factors used to predict default status. Overall, the model demonstrated that repayment history plays a significant role in credit card default behavior.

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
