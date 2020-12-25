#Find the kth smallest element in BST

class BST:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = None
		self.right = None

count=0
def kthSmallestElement(root, k):
	global count

	if not root:
		return None
	left = kthSmallestElement(root.left, k)
 
	count+=1

	if count==k:
		return root

	return kthSmallestElement(root.right, k)


if __name__ == '__main__':
	node1, node2, node3, node4, node5, node6 = BST(6), BST(3), BST(8), BST(1), BST(4), BST(7)
	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	node3.left = node6

	print(kthSmallestElement(node1, 5))


