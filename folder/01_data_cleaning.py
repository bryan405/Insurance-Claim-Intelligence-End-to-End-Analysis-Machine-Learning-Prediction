"""
01_data_cleaning.py

Health Insurance Cost & Claims Analytics (Project HIC-2026-001)
Stage 1 of 3: Data Cleaning & Preparation

Extracted directly from the project's analysis notebook (analysis.html).
Code is reproduced exactly as authored -- nothing has been changed,
only separated into its own file. Cell boundaries from the original
notebook are kept as "# %%" markers, which VS Code and Jupyter both
recognize as runnable cells.

Run this file first. It expects data.csv in the working directory
and produces the cleaned `df` used by 02_eda.py and
03_feature_engineering_modeling.py in the same session/kernel.
"""


# %%
# Imports

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
 
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
 

# %%
# one seed, used everywhere below, for reproducibility

# %%
RANDOM_STATE = 42  
pd.set_option("display.float_format", "{:.2f}".format)
sns.set(style="whitegrid", palette="Set2", font_scale=1.1)

# %%
# Load data

# %%
df = pd.read_csv("data.csv")

# %%
# Duplicate check

# %%
n_duplicates = df.duplicated().sum()
print(f"Duplicate rows found: {n_duplicates}")
if n_duplicates > 0:
    df = df.drop_duplicates()
    print(f"Duplicates dropped. Rows remaining: {len(df)}")

# %%
# Handling missing values

# %%
missing_before = df.isna().sum()
total_missing = missing_before.sum()
rows_before = len(df)
 
print("Missing values by column:")
print(missing_before[missing_before > 0])
print(f"\nTotal missing cells: {total_missing}")

# %%
# Check whether missingness is concentrated in a particular region or
# risk group before blindly dropping it — a silent drop can bias the
# training population if missingness isn't random.

# %%
if total_missing > 0 and "region" in df.columns:
    rows_with_na = df[df.isna().any(axis=1)]
    print("\nMissingness by region (rows with at least one NaN):")
    print(rows_with_na["region"].value_counts())
 
df = df.dropna()
rows_after = len(df)
pct_dropped = 100 * (rows_before - rows_after) / rows_before
print(f"\nRows before drop: {rows_before} | after: {rows_after} "
      f"| dropped: {rows_before - rows_after} ({pct_dropped:.2f}%)")
 
if pct_dropped > 5:
    print("WARNING: more than 5% of rows dropped for missingness — "
          "confirm this isn't concentrated in one segment before proceeding.")
 
assert df.isna().sum().sum() == 0, "Missing values still present after dropna()"
 

# %%
# Summary statistics

# %%
print(df.describe(include="all"))
