def max_min(A, low, high):
	if low==high:
		return (A[low], A[low])
	if low==high-1:
		return (max(A[low], A[high]), min(A[low], A[high]))
	else:
		mid = low+(high-low)//2
		left = max_min(A, low, mid)
		right = max_min(A, mid+1, high)

		return (max(left[0], right[0]), min(left[1], right[1]))



if __name__ == '__main__':
	A = [54, 26, 93, 17, 77, 31, 44, 55]
	print(max_min(A, 0, len(A)-1))