def binary_search(arr, element, start, end):
	mid = int(start + (end-start)/2)

	if start==end:
		if arr[start]==element:
			return start
		else:
			return -1

			
	if element < arr[mid]:
		return binary_search(arr, element, start, mid)
	if element > arr[mid]:
		return binary_search(arr, element, mid, end)
	if element == arr[mid]:
		return mid
	return -1

if __name__ == '__main__':
	A = [45, 54, 99, 102, 556, 10002]
	print(binary_search(A, 102, 0, len(A)-1))