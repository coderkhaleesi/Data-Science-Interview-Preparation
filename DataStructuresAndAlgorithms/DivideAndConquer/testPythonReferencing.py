#Python refencing - understand to see if mergesort creates a new array (copy)

def slicing(A):
	append_A = 10

def slicing_diff(A):
	append_A(A)

def append_A(A):
	A.append(10)

def sorted(A):
	left = A[:4]
	right = A[4:]

	left.sort()
	right.sort()


	#left[:]=[1]
	A[:] = left+right

if __name__ == '__main__':
	A = [1,2,3,4,5,0,56,7,99]
	print(A)
	#slicing(A[2:3])
	#print(A)
	sorted(A)
	print(A)
	#append_A(A)
	#print(A)