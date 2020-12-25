#Find out if a Binary Tree is BST or not 

class BST:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = None
		self.right = None

def max_node(root):

	if root is None:
		return -100
	left_max=root.data
	right_max=root.data

	if root.left is not None:
		left_max=max_node(root.left)
	if right_max is not None:
		right_max=max_node(root.right)

	return max(max(left_max, root.data), max(right_max, root.data))

def min_node(root):

	if root is None:
		return 10000
	left_min=root.data
	right_min=root.data

	if root.left is not None:
		left_min=min_node(root.left)
	if right_min is not None:
		right_min=min_node(root.right)

	return min(min(left_min, root.data), min(right_min, root.data))


def isBST(root): #O(n^2)
	
	if root is None:
		return True

	if root.left is not None and max_node(root.left) > root.data:
		return False
	if root.right is not None and min_node(root.right) < root.data:
		return False

	return isBST(root.left) and isBST(root.right)

def isBSTUtil(root, minVal, maxVal):	#Trick is to use a helper function that keeps track of the min and max. We aim to visit each node only once O(n)
	if root is None:
		return True
	if root.data <= minVal or root.data >= maxVal:
		return False
	return isBSTUtil(root.left, minVal, root.data) and isBSTUtil(root.right, root.data, maxVal)

def isBSTInorder(root, prevValue): #check why this is not correct
	if root is None:
		return True

	if not isBSTInorder(root.left, prevValue):
		return False

	if root.data < prevValue:
		return False

	print(prevValue)
	prevValue = root.data
	print(prevValue)

	if not isBSTInorder(root.right, prevValue):
		return False
	return True
	#This seems wrong because -inf is being passed at many places


if __name__ == '__main__':
	node1, node2, node3, node4, node5 = BST(6), BST(2), BST(8), BST(1), BST(9)
	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	

	print(isBST(node1))
	print(isBSTUtil(node1, float("-infinity"), float("infinity")))
	print(isBSTInorder(node1, float("-infinity")))