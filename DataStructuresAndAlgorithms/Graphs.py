#When we init the graph, the vertices are unnamed, so they are represented by an id we gave at the start. But we want to name them, we don't want them to be just a number
#That's why we have the getId functions all over. And we also want to have an index by which we access them.
#so setVertex sets the name of that index vertex. Then addEdge adds an edge between those two vertices. but now, we can refer these vertices by their names, we don't
#have to use the index anymore and the program does the conversion

class Vertex:
	def __init__(self, node):
		self.id=node
		self.visited=False
		self.distance=None

	def setVertexId(self, id):
		self.id = id

	def getVertexId(self):
		return self.id

	def getDistance(self):
		return self.distance

	def setDistance(self, distance):
		self.distance=distance

	def getConnections(self, G):
		return G.adjMatrix[self.id]

	def addNeighbour(self, neighbour, G):
		G.addEdge(self.id, neighbour)

	def setVisited(self, val):
		self.visited=val

	def __str__(self):return str(self.id)

class Graph:
	def __init__(self, numVertices, cost=0):
		self.numVertices = numVertices
		self.adjMatrix = [[-1 for i in range(numVertices)] for j in range(numVertices)]
		self.vertices = []

		for i in range(self.numVertices):
			self.vertices.append(Vertex(i))

	def setVertex(self, vtx, id):
		if 0<=vtx<=self.numVertices:
			self.vertices[vtx].setVertexId(id)

	def getVertex(self, id):
		for i in range(self.numVertices):
			if id==self.vertices[i].getVertexId():
				return i
		return -1

	def addEdge(self, frm, to, cost = 0):

		if self.getVertex(frm)!=-1 and self.getVertex(to)!=-1:
			self.adjMatrix[self.getVertex(frm)][self.getVertex(to)]=cost
			self.adjMatrix[self.getVertex(to)][self.getVertex(frm)]=cost
			print(self.adjMatrix)

	def getVertices(self):
		vertices=[]
		for i in range(self.numVertices):
			vertices.append(self.vertices[i].getVertexId())

		return vertices

	def getEdges(self):
		edges = []
		for i in range(len(self.adjMatrix)):
			for j in range(len(self.adjMatrix[0])):
				if self.adjMatrix[i][j]!=-1:
					edges.append([self.vertices[i].getVertexId(), self.vertices[j].getVertexId()])

		return edges

	def DFS(self, v, visited):
		visited[v]=True
		print("visiting",v)
		for u in range(len(self.adjMatrix[v])):
			if self.adjMatrix[v][u]!=-1 and (not visited[u]):
				self.DFS(u, visited)

	def BFS(self, v, visited):
		queue = []
		queue.append(v)

		while(len(queue)!=0):
			u = queue.pop(0)
			visited[u]=True
			print("BFS visiting", u)
			for t in range(len(self.adjMatrix[u])):
				if self.adjMatrix[u][t]!=-1 and (visited[t]==False):
					visited[t]=True
					queue.append(t)

if __name__ == '__main__':
	g = Graph(5)

	g.setVertex(0, 'a')
	g.setVertex(1, 'b')
	g.setVertex(2, 'c')
	g.setVertex(3, 'd')
	g.setVertex(4, 'e')

	print(g.getVertices())

	g.addEdge('a', 'e', 10)
	g.addEdge('a', 'c', 20)
	g.addEdge('c', 'b', 30)
	g.addEdge('b', 'e', 40)
	g.addEdge('e', 'd', 50)
	g.addEdge('f', 'e', 60)
	print(g.getEdges())

	visited = [False]*5
	g.DFS(0, visited)
	visited = [False]*5	
	g.BFS(0, visited)