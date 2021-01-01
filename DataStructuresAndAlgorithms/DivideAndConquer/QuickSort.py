#QuickSort

def quick_sort(A, left, right):
	if left<right:
		partition_point = partition(A, left, right)
		quick_sort(A, left, partition_point-1)
		quick_sort(A, partition_point+1, right)

def partition(A, left, right):
	low=left
	pivot = A[left]
	left=left+1
	done=False
	while not done:
		while(A[left]<pivot and left<=right):
			left=left+1
		while(A[right]>pivot and left<=right):
			right=right-1
		#print(A[left], A[right])
			
		if left>right:
			done=True
		else:# if A[left]>=A[right]: ->wrong condition, not mutually exclusive
			A[left], A[right] = A[right], A[left]

	A[low], A[right] = A[right], A[low]
	return right

if __name__ == '__main__':
	A=[54, 26, 93, 17, 77, 31, 44, 55]
	quick_sort(A, 0, len(A)-1)
	print(A)



