import numpy as np

def calculate(list):
    rray_3x3 = np.array(list).reshape(3, 3)

    
    mean_result = [list(np.round(np.mean(array_3x3, axis=0), 1)), list(np.round(np.mean(array_3x3, axis=1), 1)), np.round(np.mean(array_3x3), 1)]
    variance_result = [list(np.round(np.var(array_3x3, axis=0), 1)), list(np.round(np.var(array_3x3, axis=1), 1)), np.round(np.var(array_3x3), 1)]
    std_dev_result = [list(np.round(np.std(array_3x3, axis=0), 1)), list(np.round(np.std(array_3x3, axis=1), 1)), np.round(np.std(array_3x3), 1)]
    max_result = [list(np.round(np.max(array_3x3, axis=0), 1)), list(np.round(np.max(array_3x3, axis=1), 1)), np.round(np.max(array_3x3), 1)]
    min_result = [list(np.round(np.min(array_3x3, axis=0), 1)), list(np.round(np.min(array_3x3, axis=1), 1)), np.round(np.min(array_3x3), 1)]
    sum_result = [list(np.round(np.sum(array_3x3, axis=0), 1)), list(np.round(np.sum(array_3x3, axis=1), 1)), np.round(np.sum(array_3x3), 1)]
   
    calculations = {
        'mean': mean_result,
        'variance': variance_result,
        'standard deviation': std_dev_result,
        'max': max_result,
        'min': min_result,
        'sum': sum_result
    }

    return calculations
list = [14, 17, 2, 20 ,5, 20, 12, 0, 9]
result = calculate(lists)
print(result)    
    
    
