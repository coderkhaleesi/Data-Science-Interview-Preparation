#Given an array of elements A, and a key k, search for k in A. If the key is present in the array A, return the index of key in A, else return -1

def searchElement(A, i, j, k):
	if (i <= j):
	
		if A[i] == k:
			print(i)
			return i
		else:	
			return searchElement(A, i+1, j, k)
	else:
		
		return -1

if __name__=="__main__":
	
	A = [1,2,5,6,7,8, -1]
	index = searchElement(A, 0, len(A)-1, 7)
	print(index)