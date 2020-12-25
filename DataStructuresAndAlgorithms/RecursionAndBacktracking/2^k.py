#Given an integer k, find 2^k

def twoPowerk(k):
	if k==0:
		return 1

	if k<0:
		return 1/2*twoPowerk(k+1)

	else:
		return 2*twoPowerk(k-1)

if __name__=="__main__":
	print(twoPowerk(-5))