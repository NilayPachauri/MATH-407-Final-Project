import sys

def convert_to_binary(num):
	return "{:b}".format(num)

def champernowne(num):
	a = ""
	for x in range (0, num):
		a += convert_to_binary(x)

	print(a)

if __name__ == "__main__":
	champernowne(int(sys.argv[1]))