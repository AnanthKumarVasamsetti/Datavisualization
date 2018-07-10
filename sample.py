import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.hist(x, 100)
plt.title('This is a sample graph')
plt.show()