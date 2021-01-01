def sum_elems(A, low, high):

	if low==high:
		return A[low]
	elif low==high-1:
		return A[low]+A[high]
	else:
		mid = low + (high-low)//2
		sum_left = sum_elems(A, low, mid)
		sum_right = sum_elems(A, mid+1, high)

		return sum_left+sum_right

if __name__ == '__main__':
	A = [54, 26, 93, 17, 77, 31, 44, 55]
	print(sum_elems(A, 0, len(A)-1))