import pandas as pd
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

    # Assert the rows with null values are correctly identified
    assert result["null_rows"] is not None, "Null values not correctly identified"
    assert len(result["null_rows"]) == 1, "Incorrect number of rows with null values"
    
    # Check the specific row with null values
    assert result["null_rows"].iloc[0].isnull().any(), "Row with null values not correctly identified"

    # Assert the rows with duplicate values are correctly identified
    assert result["duplicate_rows"] is not None, "Duplicate values not correctly identified"
    assert len(result["duplicate_rows"]) == 2, "Incorrect number of duplicate rows"

    # Check that the duplicate rows are correctly found (Bob's row is duplicated)
    assert (result["duplicate_rows"]['Name'] == 'Bob').all(), "Duplicate values not correctly identified"

if __name__ == "__main__":
    test_findnulls_duplicates()