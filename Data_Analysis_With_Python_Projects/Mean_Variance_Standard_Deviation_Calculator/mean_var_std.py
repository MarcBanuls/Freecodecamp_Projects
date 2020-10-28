# Import Numpy
import numpy as np

def calculate(lst):
    # In case the list has the expected length, it will be reshaped to a 3x3 matrix
    if len(lst) == 9:
        reshaped = np.reshape(lst, (3,3))
    # In case the list has a different length, a ValueError is raised
    else:
        raise ValueError("List must contain nine numbers.")
    
    # Here in each key it is used a numpy function changing the axis to calculate through rows, columns and flattened (without 
    # adding an axis parameter). Also the result of the numpy array is converted to list to follow the guidelines
    # of the README.md
    calculations = {"mean": [np.mean(reshaped, axis = 0).tolist(), np.mean(reshaped, axis = 1).tolist(), np.mean(reshaped).tolist()],
                 "variance": [np.var(reshaped, axis = 0).tolist(), np.var(reshaped, axis = 1).tolist(), np.var(reshaped).tolist()],
                 "standard deviation": [np.std(reshaped, axis = 0).tolist(), np.std(reshaped, axis = 1).tolist(), np.std(reshaped).tolist()],
                 "max": [np.max(reshaped, axis = 0).tolist(), np.max(reshaped, axis = 1).tolist(), np.max(reshaped).tolist()],
                 "min": [np.min(reshaped, axis = 0).tolist(), np.min(reshaped, axis = 1).tolist(), np.min(reshaped).tolist()],
                 "sum": [np.sum(reshaped, axis = 0).tolist(), np.sum(reshaped, axis = 1).tolist(), np.sum(reshaped).tolist()]}
    
    return calculations
