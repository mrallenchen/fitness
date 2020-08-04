#Create KFOLD GRIDSEARCH WITH SAMPLING TECHNIQUES.
#return best model based on F1 score, average = "macro"

from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.dummy import DummyClassifier
from operator import itemgetter
from sklearn import tree
from sklearn.utils import check_random_state
import numpy as np
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import StratifiedKFold
import xgboost as xgb
import pandas as pd
from sklearn.metrics import classification_report

#helper function
def fold_mod_transform(scores,num):
    '''
    Input: Scores within a list (of folds) containing lists (of scores by *num* models with diff params)
    Output: (1) array with all scores, (2) array with average scores for each fold
    '''
    folds = len(scores)
    block = len(scores[0])/num
    
    s_ray = np.array(scores)
    new_mat = [[] for i in range(num)]
    for i in range(num):
        new_mat[i] = np.concatenate(s_ray[:,int(block*i):int(block*(i+1))])
    
    return new_mat

#create own scoring metric
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
lb.fit(['Athlete','Average','Fitness','Obese'])

def custom_score(y_test, y_pred_proba):
    score_points = np.array([[30,0,15,0],[0,1,-1,0],[2.5,0,100,0],[0,.0,-100,.5]])
    y_test_bin = lb.transform(y_test) #binarize the labels
    interstep = np.matmul(y_test_bin,score_points) #creates custom weights based on true value
    
    fin = interstep*y_pred_proba #raw total score
    fin_score = fin.sum()/len(fin) #average
    
    return fin_score

from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import auc
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
lb.fit(['Athelete','Average','Fitness','Obese'])

def PR_AUC_fitness(y_test,y_pred_proba):
    y_test_bin = lb.transform(y_test)
    proba = np.concatenate(y_pred_proba).reshape(len(y_pred_proba),4)
    precision, recall, _ = precision_recall_curve(y_test_bin[:, 2], proba[:, 2])
    
    return auc(recall, precision)

    
#Main function    
def SamplingGridSearchCV(resampler, model, X_train, y_train, param_grid, folds=5):
        
    kf = StratifiedKFold(n_splits=folds, shuffle = True, random_state=42)
    num_models = len(ParameterGrid(param_grid))
    # Lists to hold results
    parameters = []
    train_scores = []
    val_scores = []
    val_pred = []
    val_true = []
    val_pred_proba = []

    # Get indices for split
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    #create folds with resampling
    for indices in kf.split(X_train, y_train):
        train_ind = indices[0]
        val_ind = indices[1]
        X_tr, y_tr = X_train[train_ind], y_train[train_ind]
        X_resampled_train, y_resampled_train = resampler.fit_sample(X_tr,y_tr)
        X_val, y_val = X_train[val_ind], y_train[val_ind]
        X_resampled_val, y_resampled_val = resampler.fit_sample(X_val, y_val)
        
        
        # initialize lists to hold results for each model/parameter
        fold_parameters = []
        fold_train_scores = []
        fold_val_scores = []
        fold_y_pred = []
        fold_y_true = []
        fold_y_pred_proba = []
        
        #fit model with each parameter and append results to list for current fold
        
        if param_grid == None:
            mod = model.fit(X_tr, y_tr)    
            train_score = f1_score(y_tr, model.predict(X_tr), average='macro', zero_division = 0)
            val_score = f1_score(y_val, model.predict(X_val), average='macro', zero_division = 0)
            
            #add results to list 
            fold_parameters.append(g)
            fold_train_scores.append(train_score)
            fold_val_scores.append(val_score)
            fold_y_pred.extend(model.predict(X_val))
            fold_y_true.extend(y_val)
            fold_y_pred_proba.extend(model.predict_proba(X_val))
 
        else:
            for g in ParameterGrid(param_grid):
                model.set_params(**g)
                mod = model.fit(X_tr, y_tr)

                mod_train_pred = model.predict(X_tr)
                mod_val_pred = model.predict(X_val)


                #train_score = f1_score(y_tr, mod_train_pred, average='macro', zero_division = 0)
                #val_score = f1_score(y_val, mod_val_pred, average='macro', zero_division = 0)
                
                #train_score = custom_score(y_tr, model.predict_proba(X_tr))
                #val_score = custom_score(y_val, model.predict_proba(X_val))
                
                
                train_class = classification_report(y_tr, model.predict(X_tr), target_names = ['Athlete','Average','Fitness','Obese'], output_dict = True, zero_division=0)
                val_class = classification_report(y_val, model.predict(X_val), target_names = ['Athlete','Average','Fitness','Obese'], output_dict = True,zero_division=0)
                
                train_score = train_class['Fitness']['f1-score']
                val_score = val_class['Fitness']['f1-score']
                
                
                
                #add results to list 
                fold_parameters.append(g)
                fold_train_scores.append(train_score)
                fold_val_scores.append(val_score)
                fold_y_pred.extend(model.predict(X_val))
                fold_y_true.extend(y_val)
                fold_y_pred_proba.extend(model.predict_proba(X_val))
        
        #append results from the fold into larger list
        parameters.append(fold_parameters)
        train_scores.append(fold_train_scores)
        val_scores.append(fold_val_scores)
        val_pred.append(fold_y_pred)
        val_true.append(fold_y_true)
        val_pred_proba.append(fold_y_pred_proba)
                                   
    #aggregate all results and prepare outputs
    parameters = parameters[0]
    
    all_train_scores  = fold_mod_transform(train_scores, num_models)
    model_train_scores = np.mean(all_train_scores, axis=1)
    all_val_scores = fold_mod_transform(val_scores, num_models)
    model_val_scores = np.mean(all_val_scores, axis=1)
    
    val_pred = fold_mod_transform(val_pred, num_models)
    val_true = fold_mod_transform(val_true, num_models)
    val_pred_proba = fold_mod_transform(val_pred_proba, num_models)

   
                                   
    best_model_index = max(enumerate(model_val_scores), key=itemgetter(1))[0]
    best_params = parameters[best_model_index]
    best_model = model.set_params(**best_params)
    best_model_score = max(model_val_scores)

    scores_df = pd.DataFrame([parameters,model_train_scores,model_val_scores])
    scores_df = scores_df.rename(index={0:'parameters',1:'train',2:'val'})
    
    #print(best_model, best_model_score, best_params, model_train_scores, model_val_scores
    #print(f'f1_score(y_test, best_model.predict(X_test), average = 'macro', zero_division=0))
    #print(metrics.precision_score(y_test, best_model.predict(X_test), average = 'macro', zero_division=0))
    #print(metrics.recall_score(y_test, best_model.predict(X_test), average = 'macro', zero_division=0))
          
    return best_model, best_model_score, best_params, scores_df, best_model_index, val_pred, val_true, val_pred_proba, all_train_scores, all_val_scores




if __name__ == '__main__':
    Sampling()
   
