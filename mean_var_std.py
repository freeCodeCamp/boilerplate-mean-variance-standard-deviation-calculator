import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    calculations = {
        "mean": [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).item()
        ],
        "variance": [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).item()
        ],
        "standard deviation": [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item()
        ],
        "max": [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item()
        ],
        "min": [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item()
        ],
        "sum": [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item()
        ]
    }

    return calculations