#Dijkstra's Algorithm
#This algorithm is for weighted graphs. It cannot work if the weights are negative.
#It uses greedy method - always picks the next closest vertex to the source

#uses a priority queue to store unvisited vertices with distance from source as key

#The algorithm first starts with all vertices on the priority queue. The distance from source to all the other vertices is inf, except itself, which is 0
#Now until the priority queue is empty, the below is repeated.
#The min key vertex (distance is the key in the pq) is removed from the priority queue
#Get the neighbours of the removed vertex. Now, update their distance in the priority queue = popped_dist_from_src+cost_from_A
#Now, it might be that we can reach other nodes from the popped nodes, so we include an extra step to take the min of distance of all paths to a node


from queue import PriorityQueue
from GraphsAdjList import *

def dijkstra_path(g, source):
	pq = PriorityQueue()

	inf=float('infinity')

	for j, i in g.vertices.items():
		i.setDistance(inf)

	g.getVertex(source).setDistance(0)

	for j, i in g.vertices.items(): 
		pq.put(i.getDistance(), i.id)

	while(pq.empty() is False):
		v = pq.get()

		for u in g.getVertex(v).getNeighbors():
			if (u.getDistance() > g.getVertex(v).getDistance() + g.getVertex(v).getWeight()):
				u.setPrevious(g.getVertex(v))
				u.setDistance(g.getVertex(v).getDistance() + g.getVertex(v).getWeight())

	for v in g:
		print(v.getVertexId(), "distance", v.getDistance())

if __name__ == '__main__':
	G = Graph()
	for i in ["a", "b", "c", "d", "e"]:
		G.addVertex(i)

	G.addEdge("a", "b", 4)
	G.addEdge("a", "c", 1)
	G.addEdge("b", "e", 4)
	G.addEdge("c", "b", 2)
	G.addEdge("c", "d", 4)
	G.addEdge("d", "e", 4)

	dijkstra_path(G, "a")
