## Metis Project 3
by Allen Chen

# Fitness: Diet and Exercise

## Design:
**Motivation:** What does one need to do to achieve their ideal body type? The standard answer is "diet and exercise". 


## Deliverables:
[Slide Deck](HowToFit.pdf)\
Code:\
[Data Collection](Data_Collection.ipynb)\
[Exploratory Data Analysis](Exploratory_Data_Analysis.ipynb)\
[Modeling Initial](Modeling_Initial.ipynb)\
[Modeling Top](Modeling-Top.ipynb)\
[Modeling Script](Sampling.py)\
[Champion Modeling Script](Sampling_CHAMP.py)
- Note that the second modeling script is almost identical except for slight tweaks needed under the champion case

## Tools:
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

## General Workflow:
1. Collect Data
    - [Data ReadMe](/Data/readme.md)
    - Data primarily from NHANES
    - Stored in SQL database
    - Collected standards for target variable (body fat % standards, and BMI standards)
2. Explore and Clean Data
    - Revealed Imbalanced Data
    - Determined what Nulls to drop, turn to zero, or impute via KMeans
    - Decide on target variable classification
        - Compared using BMI or Body Fat%.
3. Select Scoring
    1. F1 score (macro and F1_fitness)
4. Modeling Loop:
    1. Features: Select Features
    2. Initial Modeling:
        - Mini-loop:
            - Pre-processing: Sampling Methods (OverSampling, SMOTE, ADASYN)
            - Cross-Validation
            - Grid Search for best hyper parameters
        - Compare Models
            - compare models by scoring metric
            - send back to feature selection
    3. Final Modeling
        - Select Top Two models and continue evaluating
            - Try a few sampling techniques
            - Try a few different features
        - Graphical options:
            - Confusion Matrix
            - PR-AUC graph
            - Feature Importance / Coefficients
    4. After selecting model, continue with 
        - Confusion Matrix
        - Feature Importance / Coefficients

Note: In reality, I went back to the data collection multiple times. I also built some of the modeling tools (such as the mini-loop script 'Sampling.py') before going back to do EDA. Then went back to data collection prior to Final Modeling to 

*If you are reading this, my lesson learned would be to be more systematic in approach. While I prioritized learning what was interesting and doing what next grabbed my attention, it would have been helpful to have spent more dedicated time early on for data collection. I tried to move too fast at times, and going back to do data over and over again was not helpful. Either do it completely right the first time around, or live with certain amount of data limitations. Definitely do not go back to look at data after every step.*

### Notes on Scoring Rationale:
- Precision: "if you do this, then outcome will definitely happen."
    - Need this high to have credibility with those who follow my advice.
- Recall: "if i promote certain strategies... how many others strategies/scenarios (outliers) am I not capturing?
    - Need this to be high, to minimize outfront critics.

- Actually both are important... I don't want to be missing any viable strategies to achieving a good weight. (So that people can choose which way they want to do things or get mad that they are an exception to my model)
- Thus, to accommodate this balance, selected F1 as the metric.
- Considered ROC-AUC for how good a model generally is, however did not pursue this because it would add additional modeling step to develop the curve.

- Custome Scoring: I also considered and implemented a custom scoring metric. However, given potential overlap and inability to use the scoring to influence the algorithms, ultimately, the F1 score would be easier to interpret and implement.




## Other References and Notes:
- [Body Fat Norms by American Counsel on Exercise](https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator/)
- [Alternative view of bf%:](https://www.fitnescity.com/blog/body-fat-percentage-chart)
- [BMI categories per CDC](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6356293/
- Class Imbalance and precision/recall curves:
    - https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/#:~:text=Generally%2C%20the%20use%20of%20ROC,moderate%20to%20large%20class%20imbalance.
    - https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc
    - https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/
