import numpy as np

def select_by_index(arr: list, indices: list, axis: int) -> np.ndarray:
    """
    Returns a 2D float64 array of the selected rows or columns.
    """
    converted = np.array(arr, np.float64)
    if axis:
        return converted[:, indices]
    else:
        return converted[indices, :]
