import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Packages import cleaning

def test_findnulls_duplicates():
    # Sample dataframe created with nulls and duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None, 'Bob', 'David'],
        'Age': [25, 30, 22, None, 30, 28]
    }

    # Convert the dict to a DataFrame
    df = pd.DataFrame(data)

    # Call the cleaning function
    result = cleaning.findnulls_duplicates(df)

    # Check for null rows in the 'Name' and 'Age' columns
    null_rows_name = result.loc['Name', 'null_rows']
    null_rows_age = result.loc['Age', 'null_rows']

    # Check for duplicate rows
    duplicate_rows = result['duplicate_rows'].iloc[0]

    # Debugging to see the value of duplicate_rows
    print(f"Duplicate count: {duplicate_rows}")

    # Assert null values
    assert null_rows_name > 0, "Null values not correctly identified in 'Name'"
    assert null_rows_age > 0, "Null values not correctly identified in 'Age'"

    duplicate_rows = int(duplicate_rows)

    # Assert duplicate values
    assert duplicate_rows > 0, "Duplicate values not correctly identified"

if __name__ == "__main__":
    test_findnulls_duplicates()