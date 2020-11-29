import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


labels = ["Single-128", "Single-256", "Single-512", "Single-1024", "Single-2048*", "Dual-512"]
x = [1.3492, 1.2455, 1.1218, 0.9440, 0.8647, 1.0011]

fig, ax1 = plt.subplots()
fig.subplots_adjust(left=0.195, right=0.88, bottom=0.15)

pos = np.arange(len(labels))

rects = ax1.barh(pos, x,
align='center', height=0.5, tick_label=labels)

ax1.set_title("Model selection")
ax1.set_xlim(0.75, 1.4)

# Plot light vertical lines for visibility
ax1.xaxis.set_major_locator(MaxNLocator(9))
ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='grey', alpha=.25)

# Plot a solid vertical gridline to highlight the median position
ax1.axvline(50, color='grey', alpha=0.25)

ax1.set_xlabel("Mean loss after 20 epochs\n*Single-2048 loss after 11 epochs")

plt.show()