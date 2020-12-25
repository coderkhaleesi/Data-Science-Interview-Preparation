#Print all possible combinations from the input string "abc". Note that "ab" is the same as "ba"

def combinations(input, s, idx):
	for i in range(idx, len(input)):
		s += input[i]
		print(f"{s}")
		combinations(input, s, i+1)
		s=s[0:-1]

if __name__ == '__main__':
	combinations("abcd", "", 0)
