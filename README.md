# Bank Deposit

Showcase project for MLOps techniques and practices.

## Introduction

### Data
Bank Marketing Dataset comes from [Kaggle Playground Series, Season 5 Episode 8](https://www.kaggle.com/competitions/playground-series-s5e8).
The dataset holds records of customers that have or have not opened a deposit account when reached through the phone by a sales rep.

### Notebooks
- [Data exploration](./notebooks/data_exploration.ipynb): investigating features and distribution. Unsurprisingly, the dataset is umbalanced.
- [Model selection](./notebooks/model_selection.ipynb): we compare different models, but since this is not a datascience project we mainly focus on "simple" stuff like pure logistic regression or XGBoost. Turns out there's not need to being fancy as these models are decent enough for the scope.


## Project management

Done with `uv`, to setup the env just do `uv sync`

### Additional dependencies
- For datascience related stuff install the dependency group `data`


## Technologies used in this project
- uv
- dvc
- MLFlow
- Docker Compose
