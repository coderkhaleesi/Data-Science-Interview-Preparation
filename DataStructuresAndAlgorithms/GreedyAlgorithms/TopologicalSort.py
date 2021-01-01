#Topological Sort

def topologicalSort(graph):

	inDegree = {v:0 for v in graph.keys()}
	sortedList = []
	inDegreeZeroQueue = []

	#First count the indegree
	for v in graph:
		for u in graph[v]:
			inDegree[u]+=1

	#Now first add initial zero indegree vertices
	for v in inDegree.keys():
		if inDegree[v]==0:
			inDegreeZeroQueue.append(v)

	while len(inDegreeZeroQueue)!=0:
		v = inDegreeZeroQueue.pop(0)
		sortedList.append(v)

		#update all indegrees connected to this v
		for u in graph[v]: 
			inDegree[u]-=1
			if inDegree[u]==0:
				inDegreeZeroQueue.append(u)

	return sortedList

if __name__ == '__main__':
	graph = {
		'Foundations':set(['Walls works']),
		'Walls works':set(['Plumbing works', 'Windows works', 'Roof works']),
		'Plumbing works':set(['Interior decorations']),
		'Windows works':set(['Interior decorations']),
		'Roof works':set(['Interior decorations']),
		'Interior decorations':set([])
	}

	result = topologicalSort(graph)
	print(result)

	if len(result) == len(graph):
		print("It's a DAG")
	else:
		print("Given graph has cycles and not possible to find topological order")