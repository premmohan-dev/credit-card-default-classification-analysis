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

<img width="800" height="477" alt="RQ1_DefaultRates" src="https://github.com/user-attachments/assets/402dcc28-1071-4f07-b2f8-db77854f2717" />

### Key Findings

Default rates varied across the major education groups. Customers with a high school education had the highest rate at 25.16%. University graduates followed at 23.73%, while graduate school attendees had the lowest at 19.23%. These results suggest that customers with higher levels of education were generally less likely to default.

### 2) How do credit limits differ between customers who default and customers who do not?

<img width="650" height="485" alt="RQ2_CreditLimits" src="https://github.com/user-attachments/assets/cca5c75e-0888-499a-b628-bab42cadb2ca" />

### Key Findings

Credit limits differed noticeably between customers who defaulted and those who did not. Customers who did not default had an average credit limit of 178,099.73, compared to 130,109.66 for customers who defaulted. Higher credit limits were generally associated with lower default rates in the dataset.

### 3) How does repayment history relate to default status?

<img width="986" height="564" alt="RQ3_RepaymentHistory" src="https://github.com/user-attachments/assets/f4512fd1-e0f6-4a20-9d1c-48725511c98a" />

Repayment status codes are defined as:

- -2 = No consumption
- -1 = Paid in full
- 0 = Use of revolving credit
- 1 = Payment delay for one month
- 2 = Payment delay for two months
- 3 = Payment delay for three months
- 4+ = Payment delays of four months or longer

### Key Findings

Default rates varied across repayment status groups. Customers with on-time or early payments had default rates between 12.81% and 16.15%. Customers with a one-month payment delay had a default rate of 33.95%, while those with delays of two months or more had default rates near 70% or higher. Overall, recent payment delays were strongly linked to a higher risk of default.

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

## SQL Analysis

The SQL queries included in this analysis were developed and tested in Microsoft Access. These queries were used to clean and summarize the dataset, calculate default rates across customer demographic groups, compare average credit limits between customers who defaulted and those who did not, and evaluate the relationship between repayment history and default status. SQL served as the primary tool for preparing and aggregating the data prior to visualization and decision tree classification modeling.

## Conclusion

This analysis found that several customer characteristics were associated with credit card default behavior. Customers with higher levels of education generally had lower default rates, while customers with higher credit limits were less likely to default on future payments. Repayment history was the strongest indicator of default risk, with default rates increasing substantially as payment delays became more severe. The decision tree model achieved an accuracy of 81.92%, showing that repayment history and other customer information can be used to predict whether a customer is likely to default. These results demonstrate how customer financial behavior can be used to better understand and predict credit card default.
