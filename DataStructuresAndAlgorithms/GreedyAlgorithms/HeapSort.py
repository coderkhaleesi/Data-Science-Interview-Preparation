def heapSort(A):

	#A won't be in a heap list form, so first we need to heapify it

	first_non_leaf = (len(A)-1)/2

	for i in range(first_non_leaf, -1, -1):
		percolate_down(A, i, len(A))

	#Now, we know A[0] is max. We keep swapping max element with last element, second last element etc. and keep
	#heapifying to get sorted array
	for i in range(len(A)-1, -1, -1):
		max_elem = A[0]
		if(max_elem > A[i]):
			A[i], A[0] = A[i], A[0]
			percolate_down(A, 0, i-1)


def percolate_down(A, first, last):
	

	while  2*first+1 <= last:
		left_child = 2*first
		right_child = 2*first+1

		if right_child>last:
			max_child = left_child
		if A[right_child] > A[left_child]:
			max_child = right_child
		else:
			max_child = left_child

		A[max_child], A[first] = A[first], A[max_child]

		first = max_child






