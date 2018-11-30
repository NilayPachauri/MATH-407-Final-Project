import numpy as np

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

# latitude of Antarctica
def antarctica_bound(num):
	return num < -(82.8628/90) and num > -1

if __name__ == '__main__':

	avg = []

	for i in range(10):
		xi, yi, zi = sample_spherical(10)

		total_zi = [x for x in zi if antarctica_bound(x)]

		avg.append(len(total_zi))
		print(len(total_zi))

	print("Average: " + sum(avg)/len(avg))