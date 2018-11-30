import numpy as np

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

# latitude of Antarctica
def antarctica_bound(num):
	return num < -(82.8628/90) and num > -1

if __name__ == '__main__':

	xi, yi, zi = sample_spherical(1000)

	print(len(zi))

	total_zi = [x for x in zi if antarctica_bound(x)]

	print(len(total_zi))