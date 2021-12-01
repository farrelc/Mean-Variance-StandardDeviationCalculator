import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr = np.array(list)
    arr = arr.reshape(3, 3)
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
    var = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
    std = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
    mx = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]
    mn = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]
    s = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
  
    calculations = {
      'mean' : mean,
      'variance' : var,
      'standard deviation' : std,
      'max' : mx,
      'min' : mn,
      'sum' : s,
    }

    return calculations