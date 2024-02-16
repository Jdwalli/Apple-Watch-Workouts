import numpy as np
import pandas as pd

def is_nan(value):
    try:
        return bool(np.isnan(value))
    except (ValueError, TypeError):
        return False

def return_first_valid_index(data:pd.DataFrame, column):
    return data[column].first_valid_index() if column in data.columns else -1