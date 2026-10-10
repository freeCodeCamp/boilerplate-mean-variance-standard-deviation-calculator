import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list, dtype=float).reshape(3, 3)

    def axis_values(func, axis):
        return func(arr, axis=axis).tolist()

    return {
        "mean": [
            axis_values(np.mean, 0),
            axis_values(np.mean, 1),
            float(np.mean(arr)),
        ],
        "variance": [
            axis_values(np.var, 0),
            axis_values(np.var, 1),
            float(np.var(arr)),
        ],
        "standard deviation": [
            axis_values(np.std, 0),
            axis_values(np.std, 1),
            float(np.std(arr)),
        ],
        "max": [
            axis_values(np.max, 0),
            axis_values(np.max, 1),
            float(np.max(arr)),
        ],
        "min": [
            axis_values(np.min, 0),
            axis_values(np.min, 1),
            float(np.min(arr)),
        ],
        "sum": [
            axis_values(np.sum, 0),
            axis_values(np.sum, 1),
            float(np.sum(arr)),
        ],
    }
