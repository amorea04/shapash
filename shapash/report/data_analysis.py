from typing import Optional

import pandas as pd

from shapash.report.common import VarType, series_dtype


def perform_global_dataframe_analysis(df: Optional[pd.DataFrame]) -> dict:
    if df is None:
        return dict()
    missing_values = df.isna().sum().sum()
    global_d = {
        'number of features': len(df.columns),
        'number of observations': df.shape[0],
        'missing values': missing_values,
        '% missing values': missing_values / df.shape[0],
    }

    return global_d


def perform_univariate_dataframe_analysis(df: Optional[pd.DataFrame]) -> dict:
    if df is None:
        return dict()
    d = df.describe().to_dict()
    for col in df.columns:
        if series_dtype(df[col]) == VarType.TYPE_CAT:
            d[col] = {
                'distinct values': df[col].nunique(),
                'missing values': df[col].isna().sum()
            }

    return d

