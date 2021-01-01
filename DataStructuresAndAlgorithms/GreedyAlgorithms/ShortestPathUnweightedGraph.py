from Graphs import *

def unweighted_shortest_path(g, source_node, visited):
	path = []
	cost = {}

	queue = []
	source = g.vertices[source_node]
	queue.append(source)
	source.setDistance(0)

	while(len(queue)!=0):
		v = queue.pop(0)
		v.visited=True

		for u in g.vertices:
			#print(g.getVertex(v.getVertexId()))
			if g.adjMatrix[g.getVertex(v.getVertexId())][g.getVertex(u.getVertexId())]!=-1 and u.visited==False:
				u.setDistance(1+v.getDistance())
				cost[u.getVertexId()]=1+v.getDistance()
				queue.append(u)
	print(cost)


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

	visited=[False]*5
	unweighted_shortest_path(g, 0, visited)


