import numpy as np

x = 7
y = -186

orientation = np.arctan2(y,  x) * (180/np.pi) % 180

print(orientation)