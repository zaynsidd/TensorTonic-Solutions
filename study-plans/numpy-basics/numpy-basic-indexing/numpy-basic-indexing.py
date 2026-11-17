import numpy as np

def extract_subarray(arr: list, row_start: int, row_stop: int, col_start: int, col_stop: int) -> np.ndarray:
    """
    Returns the selected 2D subarray with dtype float64.
    """
    converted = np.array(arr, np.float64)
    return converted[row_start:row_stop, col_start:col_stop]
