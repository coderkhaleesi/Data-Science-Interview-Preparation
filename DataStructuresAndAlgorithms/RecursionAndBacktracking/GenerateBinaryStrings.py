#Generating Binary sequences
#Generate all the binary strings with n bits

#Backtracking uses recursion because the algorithm can use the stack as an auxiliary data structure

def append(x, L):
	return [x + i for i in L]

def bit_strings(n):
	if n==0:
		return []
	if n==1:
		return ["0", "1"]

	else:
		x = (append("0", bit_strings(n-1)) + append("1", bit_strings(n-1)))
		print(x)
		return x

if __name__ == '__main__':
	bit_strings(3)

