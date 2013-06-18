import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("Lengthscale")
ticks = [-9, -6, -3, 0, 3]
labels = ["1nm", "1um", "1mm", "1m", "1km"]
plt.xticks(ticks, labels)
plt.xlim(-10, 4)

plt.savefig("/home/kyleb/src/kyleabeauchamp/personal/defense/figures/lengthscales.pdf", bbox_inches=0)
plt.axis('off')
plt.arrow(-10, 0, 4, 0)
