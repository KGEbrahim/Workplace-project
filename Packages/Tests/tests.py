import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Packages import cleaning


def test_findnulls_duplicates():
    # Create a sample DataFrame with null values and duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None, 'Bob', 'David'],
        'Age': [25, 30, 22, None, 30, 28]
    }

    df = pd.DataFrame(data)

    # Call the function
    result = cleaning.findnulls_duplicates(df)

    # Extract null_rows and duplicate_rows from the result DataFrame
    null_rows = result["null_rows"].iloc[0]  
    duplicate_rows = result["duplicate_rows"].iloc[0] 

    # Assert the rows with null values are correctly identified
    assert null_rows is not None, "Null values not correctly identified"
    
    # Check if the number of rows with null values is 1 (the row with 'None' in 'Name' and 'Age')
    assert len(null_rows) == 1, f"Expected 1 row with null values, got {len(null_rows)}"
    
    # Check that the null values are in the correct row
    assert null_rows.iloc[0].isnull().any(), "Row with null values not correctly identified"

    # Assert the rows with duplicate values are correctly identified
    assert duplicate_rows is not None, "Duplicate values not correctly identified"
    
    # Check if the number of duplicate rows is 2 (Bob's rows)
    assert len(duplicate_rows) == 2, f"Expected 2 duplicate rows, got {len(duplicate_rows)}"

    # Check that both rows with 'Bob' are identified as duplicates
    assert (duplicate_rows['Name'] == 'Bob').all(), "Duplicate values not correctly identified"


if __name__ == "__main__":
    test_findnulls_duplicates()