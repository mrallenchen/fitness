## Metis Project 3

# Fitness: Diet and Exercise -> Body Type

## Design
**Background**


**Question:** What does one need to do to achieve their ideal body type? When the standard "diet and exercise" isn't enough. I want more specifics.

Methodology:

## Data

### Source
- Downloaded data from the National Health and Nutrition Examination Survey (continuously conducted by CDC's National Center for Health Statistics) 
    - https://www.cdc.gov/nchs/nhanes/index.htm
    - NHANES 2017-2018
        - [Diet Behavior and Nutrition (DBQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DBQ_J.htm)
        - [Physical Activity (PAQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/PAQ_J.htm)
        - [Weight History (WHQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/WHQ_J.htm)
        - [Body Measures (BMX_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm)
        - [Dual-Energy X-ray Absorptiometry - Whole Body (DXX_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DXX_J.htm)
        - [Demographics (DEMO_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm)
        - [Dietary Interview (Dr1TOT_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR1TOT_J.htm)





### Pre-processing
- histogram shows there is an imbalanced problem

# **TO-DO: need to oversample**

**add discussion on undersampling, vs oversampling vs mixture**


### Scoring
- I care about precision... "if you do this, then outcome will definitely happen."
- for cross_validation. choosing the one with the best balanced_precision

# **CURRENT BLOCKER HOW TO SET SCORING FOR MULTICLASS in corss_vlaidate. I tried precision_macro, but this generates a warning"

- **However, given time, would like to create my own scoring metric**


### Algorithms
- Step 1: Determine baseline metric model using naive model of all "Obese"
- Step 2: Tune each algorithm, using CV, and find best parameters according to scoring metric
    - Decision Tree
    - KNNeighbors
    - Logistic regression
    - RandomForest
    - XGBoost
- Step 3: Compare across all of the models to choose the best Algorithm


## Deliverables


## Tools
- xport (version 3.2.1): for working with .XPT files (SAS output files used by the government). Converted the xport files to csv
- postgress - for setting up the database and SQL query
- pgadmin4 - for testing sql queries
- psycopg2 - Python-PostgreSQL Database Adapter
- pandas


## Other References
[Body Fat Norms by American Counsel on Exercise](https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator/)
