import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    rng = np.random.default_rng(seed)

    if kind=='normal':
        x = rng.normal(size=shape)
    if kind=='uniform':
        x = rng.uniform(size=shape, low = 0.0, high = 1.0)

    return np.array(x)