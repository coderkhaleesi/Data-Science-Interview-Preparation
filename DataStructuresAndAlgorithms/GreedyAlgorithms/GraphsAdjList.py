class Vertex:
	def __init__(self, id):
		self.id = id
		self.visited = False
		self.neighbors = {}
		self.previous = None

	def setVertex(self, id):
		self.id=id

	def getVertexID(self):
		return self.id

	def getDistance(self):
		return self.distance

	def setDistance(self, distance):
		self.distance=distance

	def setVisited(self):
		self.visited=True

	def getWeight(self, neighbor):
		return self.neighbors[neighbor]

	def addNeighbour(self, neighbor, cost):
		self.neighbors[neighbor] = cost

	def getNeighbors(self):
		return self.neighbors.keys()

	def getPrevious(self, prev):
		self.previous = prev

class Graph:
	def __init__(self):
		self.vertices={}
		self.num_vert = 0

	def addVertex(self, id):
		v = Vertex(id)
		self.vertices[id] = v
		self.num_vert += 1

	def getVertices(self):
		vertices = []
		for k, v in self.vertices.items():
			vertices.append(k)

		return vertices 

	def getVertex(self, id):
		if id in self.vertices:
			return self.vertices[id]
		else:
			return -1

	def getEdges(self):
		edges = []
		for k, v in self.vertices.items():
			for n in v.getNeighbors(k):
				cost = v.getWeight(n)
				edges.append([k, n.getVertexID(), cost])

		return edges

	def addEdge(self, frm, to, cost):
		if self.vertices[frm] != -1 and self.vertices[to]!=-1:
			self.vertices[frm].addNeighbour(self.vertices[to], cost)
			self.vertices[to].addNeighbour(self.vertices[frm], cost)

if __name__ == '__main__':
	g = Graph()
	g.addVertex('a')
	g.addVertex('b')
	g.addVertex('c')
	g.addVertex('d')
	g.addVertex('e')

	print(g.getVertices())

	g.addEdge('a', 'b', 4)
	g.addEdge('a', 'c', 1)
	g.addEdge('c', 'b', 2)
	g.addEdge('b', 'e', 4)
	g.addEdge('c', 'd', 4)
	g.addEdge('d', 'e', 4)

	print(g.getEdges())