import sys

def check_for_repeat(s):
	i = (s+s).find(s, 1, -1)
	return None if i == -1 else s[:i]

if __name__ == '__main__':

	x = check_for_repeat(sys.argv[1])
	if x == None:
		print("This is a unique random number");
	else:
		print("This number repeats with the following string: " + x);