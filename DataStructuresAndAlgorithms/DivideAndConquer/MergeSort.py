#Merge Sort

def merge_sort(A):

	# if len(A)==0:
	# 	return
	# if len(A)==1:
	# 	return A

	if len(A)>1:
		mid = len(A)//2

		left = A[:mid]
		right = A[mid:]

		merge_sort(left)
		merge_sort(right)

		i = j = k = 0

		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				A[k]=left[i]
				i+=1

			else:
				A[k] = right[j]
				j+=1
			k+=1
			
		while i<len(left):
			A[k]=left[i]
			k+=1
			i+=1

		while j<len(right):
			A[k]=right[j]
			j+=1
			k+=1

if __name__ == '__main__':
	A=[54, 26, 93, 17, 77, 31, 44, 55]
	merge_sort(A)
	print(A)

