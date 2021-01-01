#Minimum Set Cover Problem

def set_cover(U, subsets):
	covered = set()
	cover=[]
	elements = set(e for s in subsets for e in s)
	if elements!=U:
		return None
	while covered!=elements:
		picked_set = max(subsets, key=lambda s : len(s-covered)) #also try min(subsets, lambda s:len(elements-s))-> is of course stagnant stuck

		covered|=picked_set
		print(covered)
		cover.append(picked_set)
	return cover

if __name__ == '__main__':
	
	s1 = set([1,2,3,4,5,6])
	s2 = set([5,6,8,9])
	s3 = set([1,4,7,10])
	s4 = set([2,5,7,8,10])
	s5 = set([3,6,9,12])
	s6 = set([10, 11])
	U = set(range(1,13))
	subsets = [s1, s2, s3, s4, s5, s6]
	cover = set_cover(U, subsets)
	print(cover)

