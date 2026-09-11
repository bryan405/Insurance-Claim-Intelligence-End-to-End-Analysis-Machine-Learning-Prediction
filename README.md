**Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction**
**End-to-end data science project for insurance claim analysis and prediction using machine learning.**

## Executive Report 
**Prepared by:** Emeka Victor Agbo - Data Analyst  
**Prepared for:** Valuelink, VP of Actuarial & Business Analytics  
**Date:** September 2, 2026

# TABLE OF CONTENT

1. [EXECUTIVE SUMMARY](#executive-summary)
2. [BUSINESS CONTEXT](#business-context)
3. [DATA SOURCE,CLEANING & PREPARATION](#data-source-cleaning-&-preparation)
5. [EXPLORATORY ANALYSIS IN PYTHON](#Exploratory-analysis-iñ-python)
6. [POWER BI DASHBOARD](#power-bi-dashboard)
7. [PREDICTIVE MODELING](#predictive-modeling)
8. [PREDICTION APP](#prediction-app)
9. [RECOMMENDATIONS](#recommendations)
10. [RISK OF INACTION](#risk-of-inaction)
11. [ROADMAP / NEXT STEPS](#roadmap--next-steps)
12. [APPENDIX](#appendix)



## [EXECUTIVE SUMMARY](#executive-summary)
This report closes out the four phases requested by the VP of Actuarial & Business Analytics in August 2026: a cleaned and governed claims dataset, a self-service Power BI dashboard, a validated predictive model, and a prediction tool underwriters can use without analyst support. The short version: the data is in good shape, the dashboard is live, the model is accurate enough to support pricing conversations, and it has one systematic bias that Finance should know about before it's used to set reserves.
![Click For More Detail](doccument/Executive_Summary.pdf)

## [BUSINESS CONTEXT](#business-context)
   
In August 2026, the VP of Actuarial & Business Analytics flagged a recurring problem: the health insurance division's claims data was reviewed manually, on an ad-hoc basis, with no centralized reporting layer. Regional managers, underwriting, and executive leadership were each pulling their own cuts of the same data independently - duplicating effort and, worse, arriving at inconsistent numbers for the same questions.
![Click For More Detail](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/Business%20request%20health%20insurance%20analytics.pdf)

## [DATA SOURCE,CLEANING & PREPARATION](#data-source-cleaning-&-preparation)

 #### Dataset & Source: (Github) 
 #### Collection Method: (Download)
 #### Structure: (Csv file:1,340 Records)
 #### Data Dictionary: (id,age,gender,children,diabetic,smoker,Bmi,region,)
#### ![Preview of data Dictionary](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/model%20view.pdf)
##### Data Cleaning & Preparation
Before anything gets analyzed or modeled, it has to be trustworthy. This document walks through exactly what was done to the raw claims file to get it ready for analysis — what was checked, what was found, what was changed, and why. Nothing here is a judgment call made quietly in the background; every decision below is one a reviewer could re-run and verify.

###### Where we started
The source file (data.csv) contained 1,340 policyholder records across 10 columns: a record ID, three demographic fields (age, gender, number of children), three health-risk fields (BMI, blood pressure, diabetic status), a behavioral field (smoker status), a location field (region), and the target we ultimately want to predict or explain: claim amount.

###### Checking for duplicate records
The very first check on any new dataset is whether the same record appears more than once — duplicates silently inflate certain patterns and can make a model look more confident than it should be. A full-row duplicate check came back clean: 0 duplicate rows out of 1,340. Nothing needed to be removed at this step.

###### Finding and handling missing values
Next, every column was checked for missing values. Two columns had gaps: age was missing in 5 rows, and region was missing in 3 rows — 8 missing cells in total, spread across 8 rows (no row was missing more than one field).
Before removing anything, it's worth asking a more careful question: is this missingness spread out, or concentrated in one group? If every missing region happened to belong to smokers, for example, dropping those rows could quietly bias the dataset against that group. Here, the 8 affected rows broke down as 4 in the Northwest, 1 in the Southeast, and the remainder without a usable region - not concentrated in any single segment, and small enough (0.60% of all rows) to drop safely without distorting the population.

###### Data type and structure check
With missing values resolved, each column's data type was confirmed to match what it represents: age, BMI, blood pressure, children, and claim as numeric fields; gender, diabetic status, smoker status, and region as text categories. No type mismatches (e.g., numbers stored as text) were found.
###### Profiling the cleaned dataset
With the data cleaned, a full statistical summary confirms the dataset is sound and gives a first look at its shape:
Two things stand out even at this early stage. First, claim amount has a very large standard deviation relative to its mean - almost as large as the mean itself - which signals a right-skewed distribution with a long tail of high-cost claims rather than a tidy bell curve. Second, the categorical fields look reasonably balanced: 670 male / 662 female, 1,058 non-smokers / 274 smokers, and a fairly even split of diabetic status. None of this required any correction; it's simply useful context carried forward into the exploratory analysis in Part 2.
###### Cleaning checklist — summary
-	Duplicate rows checked — 0 found, none removed
-	Missing values identified — 8 cells across age and region
-	Missingness pattern checked for bias — confirmed spread across regions, not concentrated
-	Rows with missing values dropped — 1,340 → 1,332 rows (0.60%)
-	Zero-missing-values check re-run and passed after cleaning
-	Data types confirmed correct for every column
-	Final dataset profiled and confirmed ready for exploratory analysis


#### [DASHBOARD](#dashboard)
###### Power BI Dashboard
The dashboard is a two-page Power BI report themed to match this document so the same visual language carries from the live report into this write-up. Page 1 is the business-facing overview; Page 2 is a model-monitoring page built for the analytics team to keep an eye on the predictive model in production.


###### Health Insurance Cost and Claim Dashboard

This is the page underwriting, regional managers, and leadership will use day to day. It answers the core questions from the business request: how much are we paying out, who is driving it, and how does that break down by region, age, smoking, and health risk factors.
###### click to preview dashboard[https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/dashboard%20preview.pdf]

### KPI,                              Current Value,                              What It Tells You                         
###### Total claims                          - $17.75M                                    -Total dollar exposure across all                                                                                                 policyholders in the current filte
###### Average claim                         - $13.33K                                     -Typical payout per policyholder                                      
###### Total policyholders                   - 1332                                         -Number of policyhoders in the current                                                                                            view
###### % Smokers / % Diabetic                 - 21% / 48%                                   - Prevalence of the two health risk flags                                                                                          in the book

### What the segment charts show
-	Smoker vs. non-smoker average claim: $32K vs. $8K - a 4x gap. This is the strongest single lever in the whole dataset.
-	Diabetic vs. non-diabetic average claim: $13.4K vs. $13.2K - essentially flat. Worth a second look before treating diabetic status as a standalone pricing factor (see Section 4).
-	BMI category: the book skews heavy - 702 obese, 387 overweight, 223 normal, 20 underweight policyholders - which matters for how representative this model will be if the population shifts.
-	Claim by region: Southeast leads at $5.8M, followed by Northwest ($4.1M), Southwest ($4.0M), and Northeast ($3.9M) - driven mainly by how many policyholders are in each region, not by a materially different average cost per person.
-	Claim by age group: 31-45 carries the most total claims ($7.3M), simply because it's the largest age band in this book, not because that age group costs more per person.

<img width="2000" height="1124" alt="imagen" src="https://github.com/user-attachments/assets/498740b8-96cc-40b3-9fba-1c49fa0bef4f" />                                             <img width="2000" height="1124" alt="imagen" src="https://github.com/user-attachments/assets/1b4b4254-81ad-4de2-970c-4e21fd0e7c1a" />

                               
   ### Prediction Accuracy & Model Performance
   
 KPI        |Current value    |         Meaning                  |Business implication
------------|-----------------|----------------------------------|----------------------
Model MAE   |   $3.75K        |Average dollar miss per prediction|This is the number to quote when someone asks “how wrong is                |                 |                                  |the model, typically”
Model RMSE  |   $4.90K        |Same idea, but penalizes          |Higher than MAE confirms a handful of large misses, not                                      |big misses more                   |consistent small ones
Model R²    |   83%           |Share of claim variation the      |Strong for this type of data; leaves room for the misses                   |                 |model explains                    |discussed below
Under-      |                 |                                  |
Predicted % |   61%           |Share of policyholders whose      |The systematic bias flagged in Executive Summary 

The **“Where are the biggest misses”** table and the error-by-policyholder line chart both point the same direction: a small set of policyholders - mostly high-cost claim cases - accounts for a disproportionate share of total error, with individual misses as high as $19,563. The “over- vs. under-charging” bar chart confirms the model under-charges noticeably more often than it over-charges.

![predictive Dasboard](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/dashboard%20model.pdf)

##### Behind the dashboard: supporting exploratory visualizations
The charts below are drawn straight from the underlying Python analysis. They don't sit inside the live Power BI report, but they back up several of the KPIs and callouts above and add detail the dashboard's fixed layout doesn't have room for.
