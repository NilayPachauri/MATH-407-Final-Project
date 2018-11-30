import numpy as np
import sys

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

# latitude of Antarctica
def africa_bound(num):
	return num < -(82.8628/90) and num > -1

if __name__ == '__main__':

	avg = []
	points = int(sys.argv[1])

	for i in range(10):
		xi, yi, zi = sample_spherical(points)

		coords = [xi, yi, zi]

		print(coords)

		total_zi = [x for x in zi if africa_bound(x)]

		avg.append(len(total_zi))
		print(str(len(total_zi)) + "/" + str(points) + " = " + str(len(total_zi)/points))

	print("Average: " + str(sum(avg)/len(avg)))