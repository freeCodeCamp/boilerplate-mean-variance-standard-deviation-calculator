import numpy as np

def calculate(list):
    calculations = dict()
    if len(list) == 9:
        list = np.array(list).reshape(3,3)
        mean = [np.mean(list, axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list)]
        calculations['mean'] = mean

        variance = [np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list)]
        calculations['variance'] = variance

        stddiv = [np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list)]
        calculations['standard deviation'] = stddiv

        maximum = [np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list)]
        calculations['max'] = maximum

        minimum = [np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list)]
        calculations['min'] = minimum

        add = [np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list)]
        calculations['sum'] = add
    else:
        raise ValueError("List must contain nine numbers.")

    return calculations