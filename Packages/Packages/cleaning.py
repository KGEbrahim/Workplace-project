import pandas as pd

def findnulls_duplicates(dataframe):
    # Find the number of null values per column
    null_counts = dataframe.isnull().sum()

    # Find rows with duplicate values across the entire DataFrame
    duplicate_rows = dataframe.duplicated(keep=False)
    duplicate_count = duplicate_rows.sum()

    # Store null and duplicate info in a DataFrame
    result = pd.DataFrame({
        "null_rows": null_counts,
        "duplicate_rows": [duplicate_count] * len(dataframe.columns)
    }, index=dataframe.columns)

    return result