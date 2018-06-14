import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

plt.plot(x, y, 'purple')
plt.xlabel('X Label')
plt.ylabel('Y Lebel')
plt.title('Title')
plt.show()
