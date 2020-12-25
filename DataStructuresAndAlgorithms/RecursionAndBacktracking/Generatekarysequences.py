#Generate k-ary sequences

def possibilities(k):
	arr = []
	for i in range(k):
		arr.append(str(i))

	return arr

def karySeq(n, k):
	if n==0:
		return []
	if n==1:
		return ["0"]
	
	x = [a + b for a in possibilities(k) for b in karySeq(n-1, k)] #possibilities + recursive result
	print(x)
	return x

if __name__ == '__main__':
	karySeq(3, 4)