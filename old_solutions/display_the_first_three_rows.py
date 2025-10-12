import pandas as pd

employees = {"employee_id": [3, 90, 9, 60, 49, 43]
    , "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"]
    , "department": ["Operations", "Sales", "Engineering", "InformationTechnology", "HumanResources", "Administration"]
    , "salary": [48675, 11096, 33805, 37678, 23793, 40454]}


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)

    print(df.head(3))
    return df.head(3)