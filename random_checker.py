import sys

def principal_period(s):
	i = (s+s).find(s, 1, -1)
	return None if i == -1 else s[:i]

def convert_to_binary(num):
	return "{0:#b}".format(num)

def compute_sum_of_all_numbers_string():
	a = ""
	for x in range (0, 10):
		a += convert_to_binary(x)

	print(a)

if __name__ == '__main__':

	compute_sum_of_all_numbers_string()

	x = principal_period('004608294930875576036866359447')
	if x == None:
		print("This is a unique random number");
	else:
		print("This number repeats with the following string: " + x);

