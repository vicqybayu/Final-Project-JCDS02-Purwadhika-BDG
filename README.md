# Final-Project-JCDS02-Purwadhika-BDG
## Small Business Administration (SBA) Loan Default Prediction

Small business can help decrease unemployment rate in a country. Therefore, helping them to expand their business through loan is something that USA Small Business Administration (SBA) do. SBA helping small business by backing up a certain amount of loan that the business applied to bank. This means that the bank didn't have to take full loss if the business failed to pay the loan in full (default) which means minimizing risk the bank need to take.

In this project, i positioned myself as a loan approval officer to try to predict wether a loan will end up succesfully paid in full or defaulted. The project consisted of several steps including data preprocessing and exploratory data analysis, data visualization, and modelling.

## Data Preprocessing and Exploratory Data Analysis

The data consisted of around 900000 rows and 27 columns. The data is quite dirty, problems such as unmatch data type, missing value, and also inconsistent data existed in the dataset. I fixed all of that problem by correcting the column data type, deleting unimportant column, imputing missing value, dropping row without information to impute the missing values, eleminating outliers etc.

I added a few columns that i thought can offer more insight for the data analysis part. The columns are DaysToDisbursement, Ratio, Recession, and RealEstate. The full explanation on the data column can be read in the notebook.

## Modelling

I started this step by comparing the baseline model for three algorithm which are **logistic regression, random forest classification, and extreme gradient boosting classification**. The baseline model then evaluated using **recall** and **roc_auc** metrics for 5 fold **cross validation**.

The purpose of this step is to maximizing the recall rate of the class 1 target (default), the model then will be used to predict the outcome for all dataset, then the amount of money saved from the 
