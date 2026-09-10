**Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction**
**End-to-end data science project for insurance claim analysis and prediction using machine learning.**

## Executive Report 
**Prepared by:** Emeka Victor Agbo - Data Analyst  
**Prepared for:** Valuelink, VP of Actuarial & Business Analytics  
**Date:** September 2, 2026

# TABLE OF CONTENT

 1. [EXECUTIVE SUMMARY](#executive-summary)
2. [BUSINESS CONTEXT](#business-context)
3. [DATASET](#dataset)
4. [DASHBOARD](#dashboard)
5. [PREDICTIVE MODELING](#predictive-modeling)
6. [PREDICTION APP](#prediction-app)
7. [RECOMMENDATIONS](#recommendations)
8. [RISK OF INACTION](#risk-of-inaction)
9. [ROADMAP / NEXT STEPS](#roadmap--next-steps)
10. [APPENDIX](#appendix)



## [EXECUTIVE SUMMARY](#executive-summary)
This report closes out the four phases requested by the VP of Actuarial & Business Analytics in August 2026: a cleaned and governed claims dataset, a self-service Power BI dashboard, a validated predictive model, and a prediction tool underwriters can use without analyst support. The short version: the data is in good shape, the dashboard is live, the model is accurate enough to support pricing conversations, and it has one systematic bias that Finance should know about before it's used to set reserves.
![Click For More Detail](doccument/Executive_Summary.pdf)

## [BUSINESS CONTEXT](#business-context)
   
In August 2026, the VP of Actuarial & Business Analytics flagged a recurring problem: the health insurance division's claims data was reviewed manually, on an ad-hoc basis, with no centralized reporting layer. Regional managers, underwriting, and executive leadership were each pulling their own cuts of the same data independently - duplicating effort and, worse, arriving at inconsistent numbers for the same questions.
![Click For More Detail](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/Business%20request%20health%20insurance%20analytics.pdf)

## [DATASET](#dataset)

 #### Dataset & Source: (Github) 
 #### Collection Method: (Download)
 #### Structure: (Csv file:1,340 Records)
 #### Data Dictionary: (id,age,gender,children,diabetic,smoker,Bmi,region,)
 
#### ![Preview of data Dictionary](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/model%20view.pdf)
#### ![Preview of dataset](https://github.com/bryan405/Insurance-Claim-Intelligence-End-to-End-Analysis-Machine-Learning-Prediction/blob/main/folder/dataset.pdf)

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


