## Metis Project 3

# Fitness: Diet and Exercise -> Body Type

## Design
**Background**


**Question:** What does one need to do to achieve their ideal body type? When the standard "diet and exercise" isn't enough. I want more specifics.


Another question: Is BMI or body fat % a better metric? Can answer this by seeing how well correlated exercise

## Methodology:
1. Collect Data
    - Store in SQL database
2. Explore Data
3. Select Scoring
    1. F1 score


4. Modeling Loop:
    1. Features: Select Features
    2. Modeling Loop 1:
        - Mini-loop:
            - Pre-processing: Sampling Methods
            - Cross-Validation
            - Grid Search for best hyper parameters
        - Compare Models
            - compare models by scoring metric
            - send back to feature selection
    3. Modeling Loop 2 (Given features, Top 2 models):
        - Sampling technique
        - Graphical options:
            - Confusion Matrix
            - PR-AUC graph
            - Feature Importance / Coefficients
    4. Ensemble?
        - Save this technique for later
5. 

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
# To-Do: Webapp/Visualization <- Sunday
Plotly tree Map <- this is where I wanna be...
Plotly - dendrogram



# TO-DO: PRESENTATION <- MONDAY

# To-DO: Code-cleanup <- TUESDAY



## Tools

- SQL
    - postgress - for setting up the database and SQL query
    -  pgadmin4 - for testing sql queries
- Python libraries
    - psycopg2 - Python-PostgreSQL Database Adapter
    - pandas
    - xport (version 3.2.1): for working with .XPT files (SAS output files used by the government). Converted the xport files to csv
    - sklearn
    - seaborn
    - matplotlib

## Other References
[Body Fat Norms by American Counsel on Exercise](https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator/)

[Alternative view of bf%:](https://www.fitnescity.com/blog/body-fat-percentage-chart)


[BMI categories per CDC](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6356293/