import numpy as np
import matplotlib.pyplot as plt
from pyscript import display


# variables
x = np.linspace(0, 10, 100)
y = np.sin(x)

# the whole graph code
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color='green', label='Graph yes')
ax.set_title("Nice")
ax.grid(True)

# display it to the html
display(fig, target="graph-output")
