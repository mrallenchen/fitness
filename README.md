## Metis Project 3

# Fitness: Diet and Exercise -> Body Type

## Design
**Background**


**Question:** What does one need to do to achieve their ideal body type? When the standard "diet and exercise" isn't enough. I want more specifics.

Methodology:

## Data

# TO-DO <- IMPORT MORE DATA <- TUESDAY

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



## A discussion on imbalanced problem
- Three options here:
    - Pre-processing - resampling:
        - Undersampling: Not a great approach due to minimal data (to get the ratios reasonable, would result in reducing overall data size by a considerable amount because the )
        - Oversampling: One concern with this approach is that oversampling prior to doing a validation loop (and not during) is that it would result in overfitting where a sample is both in the train set and the validation set. Unfortunately, this would not work well with sklearn's cross_validation. To implement this properly, the validation set would need to be held out from the oversampling for the train set. Unfortunately sklearn's cross_validation does not have this functionality, and therefore any cross validation or Grid Search (for best parameters) would need to be implemented manually. As such, this approach was tabled due to time constraints. It could be a further avenue to attempt in the future to compare this approach vs. others.
        - Smote: Similar concern to the the oversampling technique, even though it would not be as drastic
    - During Model - Class Weights:
        - This one is easy to implement and makes sense for the multi-class model, by putting additional weight on the classifications that are of more interest but infrequent "athlete" and "fitness"
    - After Model - Threshold Adjustment:
        - This approach would depend on the model is not easy to implement under a multi-class model, where the classifier selects the class with the highest probability. To attempt a threshold adjustment would require building model logic from scratch and overwriting the class selection, such that some classes (given certain thresholds) would be selected in favor of others with higher probabilities. Due to the model complexity (in building and explaining) this approach was not attempted.

### Pre-processing
 - No resampling was done for this project

### Scoring
- I care about precision... "if you do this, then outcome will definitely happen."
- for cross_validation. choosing the one with the best balanced_precision

- **However, given time, would like to create my own scoring metric**

### Feature Selection!

# TO-DO ADD IN MORE FEATURES <- TUESDAY


### Algorithms
- Step 1: Determine baseline metric model using naive model of all "Obese"
- Step 2: Tune each algorithm, using CV, and find best parameters according to scoring metric
    - Decision Tree
    - KNNeighbors
        - good for multiclass
    - Logistic regression
        - 
    - RandomForest
    - XGBoost
    - Naive Bayes
        -note: for continuous and binary, will likely need to take continuous and bin it so you can binarize
        - good for bernoulli data; lots of features and minimal rows/observations
        - text class: good for multinomial Bayes
        - Naive bayes - good classifier, bad predictors -> bad proba. aka... predictions are good, but probablilies are not.
- Step 3: Compare across all of the models to choose the best Algorithm


## Deliverables
# To-Do: Webapp <- Thursday to Sunday
# TO-DO: PRESENTATION <- FRIDAY- MONDAY

# To-DO: Code-cleanup <- TUESDAY



## Tools
- xport (version 3.2.1): for working with .XPT files (SAS output files used by the government). Converted the xport files to csv
- postgress - for setting up the database and SQL query
- pgadmin4 - for testing sql queries
- psycopg2 - Python-PostgreSQL Database Adapter
- pandas


## Other References
[Body Fat Norms by American Counsel on Exercise](https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator/)
