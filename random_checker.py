def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

if __name__ = '__main__':
	print(principal_period('0045662100456621004566210045662100456621'))