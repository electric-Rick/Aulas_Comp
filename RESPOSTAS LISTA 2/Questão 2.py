import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([5,2,4,4,4,8,7,4,8,10])

plt.plot(x,y)
plt.xlabel('Tempo')
plt.ylabel('ºC')
plt.title('Vetores')
plt.show()

