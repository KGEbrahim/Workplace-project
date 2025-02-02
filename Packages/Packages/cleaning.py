import pandas as pd

def findnulls_duplicates(dataframe):
    # Find the number of null values per column
    null_counts = dataframe.isnull().sum()

    # Find duplicate rows
    duplicate_counts_row = dataframe.duplicated().sum()

    # Store null and duplicate info in a DataFrame
    result = pd.DataFrame({
        "null_rows": null_counts,
    })

    print(f"Number of row duplicates: {duplicate_counts_row}")

    return result

# Update to package version 0.31
def column_duplicates(dataframe):
    '''
    The column_duplicates function is now separated from the findnulls_duplcates function 
    to ensure a cleaner, relevant and readable result.
    '''
    # Find the number of duplicates in object data type columns
    duplicate_counts_col = dataframe.apply(lambda col: col.duplicated().sum() if col.dtype == 'object' else 0)

    # Storing result in a dataframe
    result = pd.DataFrame({
            "duplicates_column_wise": duplicate_counts_col
    })
    
    return result

# Update to package version 0.4
def duplicates_removed(dataframe):

    # Locate and store non-duplicate rows in same dataframe
    dataframe = dataframe.loc[~dataframe.duplicated()].reset_index(drop=True).copy()

    return dataframe