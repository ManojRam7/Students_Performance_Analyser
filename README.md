# Student Performance Predictor

Predicts a student's maths score from gender, ethnic group, parental education, lunch type, test
preparation course and their reading and writing scores. The project is structured as a small
training pipeline (ingestion, transformation, model selection) with a Flask app for predictions.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)

## Results

1,000 students, 80/20 split (800 / 200). Test R² from `notebook/2. MODEL TRAINING.ipynb`:

| Model | Test R² |
|---|---|
| **Ridge** | **0.881** |
| Linear regression | 0.879 (RMSE 5.42, MAE 4.23) |
| CatBoost | 0.852 |
| Random forest | 0.848 |
| AdaBoost | 0.847 |
| XGBoost | 0.828 |
| Lasso | 0.825 |
| K-nearest neighbours | 0.784 |
| Decision tree | 0.725 |

Reading and writing scores explain most of the variance, which is why the linear models beat the
tree ensembles here; the training pipeline keeps whichever model scores best and refuses to save one
below R² 0.6.

## Approach

- **EDA** (`notebook/1 . EDA STUDENT PERFORMANCE .ipynb`): no missing values or duplicates;
  total and average scores added; female students and students with a standard lunch or a completed
  test-preparation course score higher on average; groups A and B score lowest.
- **Modelling** (`notebook/2. MODEL TRAINING.ipynb`): one-hot encoding of the categorical fields,
  scaling, and nine regressors compared on the same split.
- **Pipeline** (`src/components/`): `data_ingestion.py` splits the raw data into `artifacts/`,
  `data_transformation.py` builds and saves the preprocessor, `model_trainer.py` trains the
  candidates and saves the best model.
- **App** (`application.py`): a form at `/predictdata` that runs the saved preprocessor and model.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.pipeline.train_pipeline     # retrain; writes artifacts/model.pkl and preprocessor.pkl
python application.py                     # http://127.0.0.1:5000
```

## Project structure

```text
application.py              Flask app (app.py imports it for hosting)
src/components/             data_ingestion, data_transformation, model_trainer
src/pipeline/               train_pipeline, predict_pipeline
src/utils.py, logger.py, exception.py
notebook/                   EDA, model training, data
artifacts/                  train/test splits, preprocessor, model
templates/                  home and prediction pages
```
