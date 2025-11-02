# Bank Deposit

Showcase project for MLOps techniques and practices.

## Introduction

### Data
Bank Marketing Dataset comes from [Kaggle Playground Series, Season 5 Episode 8](https://www.kaggle.com/competitions/playground-series-s5e8).
The dataset holds records of customers that have or have not opened a deposit account when reached through the phone by a sales rep.

### Notebooks
- [Data exploration](./notebooks/data_exploration.ipynb): investigating features and distribution. Unsurprisingly, the dataset is umbalanced.
- [Model selection](./notebooks/model_selection.ipynb): we compare different models, but since this is not a datascience project we mainly focus on "simple" stuff like pure logistic regression or XGBoost. Turns out there's not need to being fancy as these models are decent enough for the scope.

### Experiment tracking and model+data versioning
MLFlow is used to log and easily compare different kinds of models and their performances, it also record the dataset version.

For this setup, I choose to keep the data locally. In a production setting you would like to version models on remote storage and keep runs on a DB.

DVC helps to version data along with code, in this configuration we keep the data on local storage, but it's easy to push them to an S3 bucket or even a Google Drive folder.

## Project management

Done with `uv`, to setup the env just do `uv sync`

### Additional dependencies
- For datascience related stuff install the dependency group `data`


## Technologies used in this project
- uv
- dvc
- MLFlow
- Docker Compose
