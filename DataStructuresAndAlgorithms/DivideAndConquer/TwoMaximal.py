#Return the largest two elements in an array

def two_maximal(A, low, high):
	if low==high:
		return (A[low], A[high])
	if low==high-1:
		if A[low]>A[high]:
			return (A[low], A[high])
		else:
			return (A[high], A[low])

	mid = low + (high-low)//2
	left = two_maximal(A, low, mid)
	right = two_maximal(A, mid+1, high)

	if left[0] >= right[0]:
		max1 = left[0]
		max2 = right[0]
		if max2 < left[1]:
			return (max1, left[1])
		else:
			return (max1, max2)
	else:
		max1 = right[0]
		max2 = left[0]

		if max2 < right[1]:
			return (max1, right[1])
		else:
			return (max1, max2)


if __name__ == '__main__':
	A = [54, 26, 93, 17, 77, 31, 44, 55]
	print(two_maximal(A, 0, len(A)-1))