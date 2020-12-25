#Given an array, check whether the array is in sorted order with recursion

def checkSortedArray(A):
	if len(A)==1:
		return True

	return A[0] <= A[1] and checkSortedArray(A[1:])


if __name__=="__main__":
	
	A = [1,2,5,6,7,8]
	print(checkSortedArray(A))
	