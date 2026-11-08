import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    df = pd.DataFrame(data)
    return {'data' : df.to_dict("list"),
    'shape' : list(df.shape),
    'columns' : df.columns.tolist()}