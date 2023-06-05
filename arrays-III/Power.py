
def modularExponentiation(x, n, m):
	if n==0:
		return 1.0
	if n < 0:
		n= -1 * n
		x = 1/x
	result = 1
	while n!=0:
		if n%2==1:
			n-=1
			result *=x
		x = x * x
		n = n/2
	return result%m 