def findnulls_duplicates(dataframe):
    result = {
        "null_rows": None,
        "duplicate_rows": None
    }

    # Find rows with null values
    null_values = dataframe[dataframe.isnull().any(axis=1)]
    if not null_values.empty:
        result["null_rows"] = null_values

    # Find rows with duplicate values
    duplicate_values = dataframe[dataframe.duplicated(keep=False)]
    if not duplicate_values.empty:
        result["duplicate_rows"] = duplicate_values

    return result