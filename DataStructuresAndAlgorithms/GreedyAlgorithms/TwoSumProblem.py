#Two Sum Problem
#Given an array of elements along with a constant K, write an algorithm to find out whether two nums exist that sum to K

def twoSumBruteForce(A, K):
	for i in A:
		for j in A:
			if (A[i]+A[j] == K):
				return A[i],A[j]

def twoSumSorting(A, k):
	A.sort()
	begin=0
	end=len(A)-1
	while begin < len(A) and begin<=end:
			if (A[begin]+A[end] < k):
				begin+=1
			elif (A[begin]+A[end] > k):
				end-=1
			else:
				return A[begin], A[end]

def twoSumHashing(A, k):
	sum_hash = {}

	for i in A:
		if i in sum_hash:
			sum_hash[i]+=1
		else:
			sum_hash[i] = 1

	for i in A:
		if k-i in sum_hash:
			return i, k-i

if __name__ == '__main__':
	A =[3,5,2,4,6,7,7,8,12876, 44, 11]
	print(twoSumBruteForce(A, 12))
	print(twoSumSorting(A, 10))
	print(twoSumHashing(A, 12878))