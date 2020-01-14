import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500
grey_h = 28 + 4 * np.random.randn(greyhounds)
labs_h = 24 + 4 * np.random.randn(labs)

plt.hist([grey_h, labs_h], stacked=True, color=['r', 'b'])
plt.show()
