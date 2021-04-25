import json
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.plot(squares)

plt.show()
