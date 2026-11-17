import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.array(data, np.float64)
    if operation == 'flatten':
        rsp = len(data) * len(data[0])
        return np.reshape(data, (rsp,))
    elif operation == 'transpose':
        return data.T.copy()
    elif operation == 'add_batch':
        return np.reshape(data, (1, len(data), len(data[0])))