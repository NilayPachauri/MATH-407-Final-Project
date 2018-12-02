import numpy as np
import sys

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

# return true if within the latitude and longitude of Africa
def africa_bound(num):
	bounding_box = ((num[2] < (35/90) and num[2] > -(35/90)) and (num[0] > -(14/90) and num[0] < (50/90))) 
	ocean_box = (num[2] < (2/90) and num[2] > -(35/90)) and (num[0] > -(14/90) and num[0] < (15/90))
	return bounding_box and not ocean_box

if __name__ == '__main__':

	avg = []
	points = int(sys.argv[1])

	for i in range(10):
		xi, yi, zi = sample_spherical(points)

		coords = []

		for j in range(len(xi)):
			coords.append([xi[j], yi[j], zi[j]])

		total_zi = [x for x in coords if africa_bound(x)]

		avg.append(len(total_zi))
		print(str(len(total_zi)) + "/" + str(points) + " = " + str(len(total_zi)/points))

	print("Average: " + str((sum(avg)/len(avg))/points))