# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a  machine learning model that trains on [Census Bureau Data](https://archive.ics.uci.edu/dataset/20/census+income) data using hyperparameters and then saves the model.

- Model Type: RandomForestClassifier
- Trained with scikit-learn version: 1.0.2
- Model Hyperparameters: Default scikit-learn hyperparameters

## Intended Use
This model is used to predict the whether a person makes more than $50K/year or less than $50K/year, based on data features. 

## Training Data
- The training data has 26048 rows and 15 features(columns). This was derived from using 80% of the original 48842 records. 
- The features of the dataset are as follows: age, workclass, fnlgt, education, education-num, marital-status,occupation,relationship,race,sex, capital-gain, capital-loss, hours-per-week, native-country, salary.
- This model uses only the 8 categorical features: workclass, education, marital-status, occupation, relationship, race, sex, native-country.
- One Hot Encoder was used on the features and a label binarizer was used on the labels.
- The target of this model is "salary."

## Evaluation Data
- The test data has 6513 rows and the same 15 features. This was derived from using 20% of the original 48842 records.
- The features of the dataset: age, workclass, fnlgt, education, education-num, marital-status,occupation,relationship,race,sex, capital-gain, capital-loss, hours-per-week, native-country, salary.
- This model uses only the 8 categorical features: workclass, education, marital-status, occupation, relationship, race, sex, native-country.
- The target of the model is "salary."

## Metrics
Metrics used and model performance:
- Precision: 0.7677
- Recall: 0.6292
- F1: 0.6916

The performance of model slices can be found in slice_output.txt

## Ethical Considerations
Any time age, marital status, race and sex are included in decision-making there is potential for discrimination. There may also be legal implications around decision-making using these features.

## Caveats and Recommendations
This data was donated to the census bureau on 4/30/1996. It is no longer representational of current conditions. Even the breakpoint of $50k seems outdated. Consider updating this data for better accuracy.
