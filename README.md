## Metis Project 3

# Fitness: Diet and Exercise -> Body Type



## Design
**Background**


**Question:** What does one need to do to achieve their ideal body type? When the standard "diet and exercise" isn't enough. I want more specifics.


Another question: Is BMI or body fat % a better metric? Can answer this by seeing how well correlated exercise

Methodology:

## Data

# TO-DO <- Compare ACE/BF vs BMI view
https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html



# EDA insights are important
# feature importance
# model 
# model - confusion matrix

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

## Feature Engineering
- Do I need to make anything One-hot?
- Do I need to bin anything?

### Scoring
- Precision: "if you do this, then outcome will definitely happen."
    - Need this high to have credibility with those who follow my advice.
- Recall: "if i promote certain strategies... how many others strategies/scenarios (outliers) am I not capturing?
    - Need this to be high, to minimize outfront critics.

- Actually both are important... I don't want to be missing any viable strategies to achieving a good weight. (So that people can choose which way they want to do things or get mad that they are an exception to my model)
- Will opt for F1 metric.
- do care about ROC-AUC for how good a model generally is
- and then use a ROC

- for cross_validation. choosing the one with the best balanced_precision

- because of class imbalance, will look at precision/recall curves.
https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/#:~:text=Generally%2C%20the%20use%20of%20ROC,moderate%20to%20large%20class%20imbalance.

On a single metric - want to look at F1
https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc
https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/


## Modeling

### Pre-processing
 - No resampling was done for this project
  - For future if interested: kf.split will split things, and using indicies acan pull these... grab those indices and then apply those to train/val sets... can resample for the train



- **However, given time, would like to create my own scoring metric**

### Feature Selection!

# TO-DO ADD IN MORE FEATURES <- TUESDAY


### Algorithms
## TO-DO: 1. Do a initial model search, using kfold cross validation with various resampling techniques. Can then save and graph ROC curves for each model
## To-DO: 2. Pick the few models that work best then gridsearch for hyperparameters
## Can switch step 1 or 2...
## consider yellowbrick for feature importance chart
- Step 1: Determine baseline metric model using naive model of all "Obese"
- Step 2: Tune each algorithm, using CV, and find best parameters according to scoring metric
    - Big 3 for classification: XGBoost, Random Forest, logisitic Regression
    - Big 4 for regression??: Poission regression great for count data, Linear regression / XGBoost regression , Time Series regression (ARIMA)
    - Decision Tree
    - KNNeighbors
        - good for multiclass
    - Logistic regression
        - 
    - RandomForest (bagging)
        - can get feature importance, hard to interpret trees
         - not great for regression (slow, gradient boosted regressino will be better though)
    - XGBoost (boosting)
        - can get feature importance, hard to interpret trees
        - feature importance gain for XGBoost almost the same as RandomForest feature importance
    - Naive Bayes
        -note: for continuous and binary, will likely need to take continuous and bin it so you can binarize
        - good for bernoulli data; lots of features and minimal rows/observations
        - text class: good for multinomial Bayes
        - Naive bayes - good classifier, bad predictors -> bad proba. aka... predictions are good, but probablilies are not.
    - xgBoost
    - softmax?
- Step 3: Compare across all of the models to choose the best Algorithm

Note: 
- should use Precision-Recall curves: 
https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/#:~:text=Generally%2C%20the%20use%20of%20ROC,moderate%20to%20large%20class%20imbalance.


## Deliverables
# To-Do: Webapp <- 
Plotly tree Map <- this is where I wanna be...
Plotly - dendrogram



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

[Alternative view of bf%:](https://www.fitnescity.com/blog/body-fat-percentage-chart)
[BMI categories per CDC](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6356293/