import pandas as pd

def findnulls_duplicates(dataframe):
    # Find rows with null values
    null_rows = dataframe[dataframe.isnull().any(axis=1)]
    
    # Find rows with duplicate values
    duplicate_rows = dataframe[dataframe.duplicated(keep=False)]

    # Store in dataframe
    result = pd.DataFrame({
        "null_rows": [null_rows if not null_rows.empty else pd.DataFrame()],
        "duplicate_rows": [duplicate_rows if not duplicate_rows.empty else pd.DataFrame()]
    })

    return result