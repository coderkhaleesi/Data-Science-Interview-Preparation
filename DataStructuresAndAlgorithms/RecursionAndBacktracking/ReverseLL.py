#Reverse a Linked List

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, val):
		self.data = val

	def setNext(self, nextNode):
		self.next = nextNode

def reverseLL(llHead):
	if llHead is None or llHead.next is None:
		return llHead
	print(llHead.data)
	temp = llHead.next
	llHead.next = None
	reversed = reverseLL(temp)
	temp.next = llHead #I had made a mistake here by writing reversed.next=llHead which will obviously print 5, 1 and not 5, 4, 3, 2, 1
	
	return reversed

def reverseLLIterative(llHead):
	if llHead is None or llHead.next is None:
		return llHead
	prev = None
	current = llHead
	while current is not None:
		temp = current.next
		current.next = prev
		prev = current
		current = nextNode

	head = prev
	return prev


def traverseLinkedList(ll):
	print(ll.getNext())
	while ll is not None:
		print(f"The value is {ll.data}")
		ll = ll.getNext()

if __name__ == '__main__':

	n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)

	n1.setNext(n2)
	n2.setNext(n3)
	n3.setNext(n4)
	n4.setNext(n5)

	traverseLinkedList(n1)

	reversedLL = reverseLL(n1)
	traverseLinkedList(reversedLL)

