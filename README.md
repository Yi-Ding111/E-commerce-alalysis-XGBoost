# E-commerence consumer data analysis with business analysis model and XGBoost prediction

This project uses python to connect MySQL in local and does analysis: _data preview, screening analysis objects, EDA, using Business Analysis Framework (AARRR Framework, Funnel analysis and RFM model) and XGBoost._

The py files in folders (1,2,3,4,5) mainly for sql query with python version doing the data preview and plots. folder 6 includes 4 versions for XGBoost. 

**For easy to keep output, All output is annotated below the corresponding code, including some sql query and tableau query and calculation. So this document can be a reference** 

## Data preview

Folder-1: _a view of all data distribution_ is the preview of data distribution. The purpose is to understand data.

Folder-2 to folder-3: visualization, print plot to find the features and trends of one specific category. 

## Business analysis model

Folder-5: the code of process of business analysis framework (AARRR framework, Funnel analysis and RFM model) and visualization.

> AARRR.py

> image drawing.R

## Data clean, integration, prediction

The folder-6: including EDA with different versions data clean and data integration,data transform and XGBoost prediction. 
The final prediction 

>xgboost_top10_week.ipynb

accuracy (r-square) can arrive **around 0.80**.

___
___
Project created at Dec 2020

## Contact

Author: Yi Ding

email: dydifferent@gmail.com


