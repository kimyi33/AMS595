# This python file computes the Mandelbrot set over the range [−2, 1] × [−1.5, 1.5] using a threshold of 50.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
threshold = 50    # |z| < threshold
num_pts = 1000     # the number of grid points for each axis.
maximum_iteration = 250       # a maximum number of iterations.

# Generate points over the range [−2, 1] × [−1.5, 1.5].
x_range, y_range = np.mgrid[-2:1:num_pts*1j, -1.5:1.5:num_pts*1j]

# Set c = x + 1j * x
c_range = x_range + 1j *y_range

# mask will indicate which points are in Mandelbrot set
mask = np.zeros((num_pts, num_pts))

# Check whether each point is in Mandelbrot set or not.
for i in range(num_pts):
    for j in range(num_pts):
        c = c_range[i,j]
        z = 0
        iterations = 0

        while abs(z) < threshold and iterations < maximum_iteration:
            z = z*z + c
            iterations += 1
        # If z does not diverges, it is in the Mandelbrot set
        if iterations == maximum_iteration:
            mask[i, j] = 1

# Plotting
plt.imshow(mask.T, extent=(-2, 1, -1.5, 1.5)) #plt.imshow() plots the first index on the y-axis, and the second index on the x-axis
plt.gray()
plt.title('Mandelbrot Set Visualization')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.savefig('mandelbrot.png')
plt.show()