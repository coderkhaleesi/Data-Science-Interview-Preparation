class ConnectedCells:

 	def __init__(self, matrix):
 		self.matrix = matrix
 		self.m = len(matrix)
 		self.n = len(matrix[0])
 		self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
 		self.max_size = -1

 	def max_region_size(self):
 		for i in range(len(self.matrix)):
 			for j in range(len(self.matrix[0])):
 				region_size = self.find_region_size(i, j)
 				if region_size > self.max_size:
 					self.max_size = region_size

 		return self.max_size


 	def find_region_size(self, i, j):
 		if i>=self.m or i<0 or j<0 or j>=self.n:
 			return 0
 	

 		elif self.matrix[i][j] == 0 or self.visited[i][j]==True:
 			return 0
 		else:
 			self.visited[i][j] = True
 			return 1 + self.find_region_size(i-1, j) \
 			+ self.find_region_size(i-1, j-1) \
 			+ self.find_region_size(i-1, j+1) \
 			+ self.find_region_size(i, j-1) \
 			+ self.find_region_size(i, j+1) \
 			+ self.find_region_size(i+1, j-1) \
 			+ self.find_region_size(i+1, j+1) \
 			+ self.find_region_size(i+1, j) \

if __name__ == '__main__':
 	A = [[1,1,0,0,0],
 		 [0,1,1,0,0],
 		 [0,0,1,0,1],
 		 [1,0,0,0,1],
 		 [0,1,0,1,1]]

 	cc = ConnectedCells(A)
 	print(cc.max_region_size())






 #in order to backtrack using stack, one of the arguments should be the 
 #possibilities you want to backtrack on, for eg pathfinding alo should 
 #have the position as agument because otherwise how will you go back to a previous position