import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  return np.array( x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)   # xの範囲を-5.0から5.0で0.1刻みで表示
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)             # yの範囲を-0.1から1.1とする
plt.show()