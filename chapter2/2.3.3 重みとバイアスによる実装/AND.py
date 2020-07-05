import numpy as np
def AND(x1, x2):
  x = np.array([x1, x2])
  x1 = 0.8
  x2 = 0.2
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return print(0)
  else:
    return print(1)