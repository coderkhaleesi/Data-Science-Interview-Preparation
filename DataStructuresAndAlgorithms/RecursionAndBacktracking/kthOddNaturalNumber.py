#Given a positive integer k, find the kth odd natural number

def kOddNum(k):
	if k==1:
		return 1
	else:
		return 2 + kOddNum(k-1)

if __name__=="__main__":
	print(kOddNum(7))