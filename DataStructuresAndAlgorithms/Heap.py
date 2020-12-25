#Heaps
#Properties:
#The value of a node must be greater than or equal to OR less than or equal to than the values of its children
#All leaves should be at h or h-1


class Heap(object):
	"""docstring for Heap"""
	def __init__(self, heap_list=[0]):
		super(Heap, self).__init__()
		self.heap_list = heap_list
		self.size = 0

	def parent(self, index):
		return index/2

	def children(self, index):
		return 2*index, 2*index+1

	def get_max(self):
		return self.heap_list[0]

	def percolate_down(self, i):

		while 2*i <= self.size:
			index = self.get_max_child(i)
			if self.heap_list[i-1] < self.heap_list[index-1]:
				self.heap_list[i-1], self.heap_list[index-1] = self.heap_list[index-1], self.heap_list[i-1]


	def get_max_child(self, i):
		
		if 2*i+1 > self.size:
			return 2*i
		left_child, right_child = self.children(i)

		if self.heap_list[left_child-1] < self.heap_list[right_child-1]:
			return 2*i

		else:
			return 2*i + 1

	def 




		