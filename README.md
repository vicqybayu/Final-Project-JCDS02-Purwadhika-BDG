# Final-Project-JCDS02-Purwadhika-BDG
## Small Business Administration (SBA) Loan Default Prediction

Small business can help decrease unemployment rate in a country. Therefore, helping them to expand their business through loan is something that USA Small Business Administration (SBA) do. SBA helping small business by backing up a certain amount of loan that the business applied to bank. This means that the bank didn't have to take full loss if the business failed to pay the loan in full (default) which means minimizing risk the bank need to take.

In this project, i positioned myself as a loan approval officer to try to predict wether a loan will end up succesfully paid in full or defaulted. The project consisted of several steps including data preprocessing and exploratory data analysis, data visualization, and modelling.

## Data Preprocessing and Exploratory Data Analysis

The data consisted of around 900000 rows and 27 columns. The data is quite dirty, problems such as unmatch data type, missing value, and also inconsistent data existed in the dataset. I fixed all of that problem by correcting the column data type, deleting unimportant column, imputing missing value, dropping row without information to impute the missing values, eleminating outliers etc.

I added a few columns that i thought can offer more insight for the data analysis part. The columns are DaysToDisbursement, Ratio, Recession, and RealEstate. The full explanation on the data column can be read in the notebook.

## Modelling

I started this step by comparing the baseline model for three algorithm which are **logistic regression, random forest classification, and extreme gradient boosting classification**. The baseline model then evaluated using **recall** and **roc_auc** metrics for 5 fold **cross validation**.

![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Model%20Performance.PNG?raw=true)

XGBoost gave us the best performance for both ROC AUC and Recall metrics, thus this model will be the one used for the dataset.

The purpose of this step is to maximizing the recall rate of the class 1 target (default). The model then will be used to predict the outcome for all dataset, then the amount of money saved will be calculated for each optimization.

The final model that is chosen is the model trained without a few features such as
- ApprovalDate
- CreateJob
- RetainedJob
- DisbursementDate
- GrAppv
- DaysToDisbursement

and also by looking at the ROC AUC curve, the model performed better when the probability threshold are decsreased. Thus the final model is using 0,37 as the probability threshold for the prediction. Above 0,37 will be considered default, and below will be considered paid in full. Below is the classification report.

![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Classification%20Report.PNG?raw=true)

This model can detect 90 percent of defaulted loan and resulting in more than **7 billion dollar** saved from the previous loan data in the dataset. I personally believe this model is can help loan officer to better analyze an incoming loan application.

## Dashboard

### Prediction Home
![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Screenshot%20(49).png?raw=true)

### Prediction Result
![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Screenshot%20(52).png?raw=true)

### Dataset
![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Screenshot%20(50).png?raw=true)

### Data Visualization
![alt tag](https://github.com/vicqybayu/Final-Project-JCDS02-Purwadhika-BDG/blob/master/Github%20Markdown%20Image/Screenshot%20(51).png?raw=true)

## Conclusions
- XGB Classifier with baseline parameter and 0.37 threshold gives 0.90 recall performance on the model, meaning 90% default loan is succesfully predicted by the model.
- The final model gives 0.97 roc auc score, this means the model have a great performance in predicting wether a loan will be paid in full or ended up defaulted.
- Around 7 billion dollar of past loan can be saved using this model.
- There's no interest rate for each loan application, thus we can't calculate the profit from the each loan. This made us unable to consider how much profit we can get thus only loss prevention considered to be the most important aspect of model selection. 
