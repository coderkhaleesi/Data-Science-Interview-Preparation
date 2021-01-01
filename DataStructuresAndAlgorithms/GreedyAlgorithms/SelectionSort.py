#Selection Sort is a greedy algorithm. It's based on finding the smallest element in the array and putting it in its right position in a sorted array

def selection_sort(A):
	for i in range(len(A)):
		for j in range(i, len(A)):
			if A[j] < A[i]:
				A[i], A[j] = A[j], A[i]

	return A

if __name__ == '__main__':
	A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(selection_sort(A))
