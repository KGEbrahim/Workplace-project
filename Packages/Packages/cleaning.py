import pandas as pd

def findnulls_duplicates(dataframe):
    # Find the number of null values per column
    null_counts = dataframe.isnull().sum()

    # Find the number of duplicate values per column
    duplicate_counts_col = dataframe.apply(lambda col: col.duplicated().sum())

    # Find duplicate rows
    duplicate_counts_row = dataframe.duplicated().sum()

    # Store null and duplicate info in a DataFrame
    result = pd.DataFrame({
        "null_rows": null_counts,
        "duplicates_column_wise": duplicate_counts_col
    })

    # Add row-wise duplicates
    result["duplicate_rows"] = duplicate_counts_row

    return result