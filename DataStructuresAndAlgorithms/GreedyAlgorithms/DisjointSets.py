# Implement Fast UNION (Slow FIND), Fast UNION (Quick FIND), and Fast UNION by path compression

class DisjointSet:
	def __init__(self, n):
		self.X = []
		self.makeset(n)

	def makeset(self, n):
		self.X = [i for i in range(n)]

	def find(self, element): #slow find
		if (self.X[element]==element):
			return element
		return self.find(self.X[element])

	def union(self, elem1, elem2):
		self.X[self.find(elem1)] = self.find(elem2)

class DisjointSetQuickFind:
	def __init__(self, n):
		self.X=[]
		self.makeset(n)

	def makeset(self, n):
		self.X = [-1 for i in range(n)]

	def find(self, element):
		if(X[element] < 0):
			return element
		else:
			self.find(X[element])

	def union(self, elem1, elem2):
		root1 = self.find(elem1)
		root2 = self.find(elem2)

		if root1==root2:
			return
		if self.X[root2] < self.X[root1]:
			self.X[root2] += self.X[root1]
			self.X[root2]=root1
		else:
			self.X[root1] += self.X[root2]
			self.X[root1]=root2

#https://www.youtube.com/watch?v=kaBX2s3pYO4&ab_channel=TECHDOSE
#https://algorithms.tutorialhorizon.com/disjoint-set-union-find-algorithm-union-by-rank-and-path-compression/#:~:text=Union%20by%20rank%20always%20attaches,and%20a%20rank%20of%20zero.&text=Both%20trees%20have%20the%20different,the%20larger%20of%20the%20two.


#Union by size - Make the smaller tree a subtree of the larger tree
#Union by height - Make the tree with less height a subtree of the tree with more height