import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:
    """
    Returns a 2D float64 array of zeros or ones with the requested shape.
    """
    if 'zeros' == kind:
        return np.zeros(shape, np.float64)
    elif 'ones' == kind:
        return np.ones(shape, np.float64)
        
