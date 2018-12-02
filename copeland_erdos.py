from math import sqrt
import sys

def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

def convert_to_binary(num):
	return "{:b}".format(num)

def copeland_erdos(num):
	a = ""
	for x in range (0, num):
		if prime(x):
			a += convert_to_binary(x)

	print(a)

if __name__ == "__main__":
	copeland_erdos(int(sys.argv[1]))