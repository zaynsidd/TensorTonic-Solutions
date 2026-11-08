import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    df = pd.DataFrame(data)
    return {'rows':df.shape[0], 
           'cols': df.shape[1],
            'columns' : df.columns.tolist(),
           'total_values' : df.shape[0]*df.shape[1],
           'dtypes' : df.dtypes.astype('str').to_dict()}
