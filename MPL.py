import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 1000)
y1 = x**99


fig = plt.figure()
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Velocity")
plt.plot(x, y1)
fig.savefig("cosfig")