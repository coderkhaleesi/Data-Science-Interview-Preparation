

def pathFinder(A, position, n):
	i, j = position[0], position[1]

	if position == (n-1, n-1):
		return [(n-1, n-1)]
	if A[i][j] == 0:
		return None
	if i+1 < n and A[i+1][j]==1:
		a = pathFinder(A, (i+1, j), n)
		if a!=None:
			return [(i, j)] + a
	if j+1 < n and A[i][j+1]==1:
		b = pathFinder(A, (i, j+1), n)
		if b!=None:
			return [(i, j)] + b


initPos =(0, 0)
A = [[1,1,0,0,0],
 		 [0,1,1,0,0],
 		 [0,0,1,0,1],
 		 [1,0,1,1,1],
 		 [0,1,0,1,1]]

n = len(A)
print(pathFinder(A, initPos, n))