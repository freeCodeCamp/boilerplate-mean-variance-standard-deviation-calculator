import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers, dtype=float).reshape(3, 3)

    return {
        "mean": [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            float(np.mean(matrix)),
        ],
        "variance": [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            float(np.var(matrix)),
        ],
        "standard deviation": [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            float(np.std(matrix)),
        ],
        "max": [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            float(np.max(matrix)),
        ],
        "min": [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            float(np.min(matrix)),
        ],
        "sum": [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            float(np.sum(matrix)),
        ],
    }

if __name__ == "__main__":
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
