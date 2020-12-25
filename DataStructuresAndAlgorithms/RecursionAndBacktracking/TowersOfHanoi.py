#Recursion is good for sort, search and traveral probmes. Basically for tasks that can be defined in terms of smiliar subtasks
#First identify the base case
#You need courage for recursion

def towersOfHanoiMove(number, src, aux, dest):

	if number>=1:
		towersOfHanoiMove(number-1, src, dest, aux)
		moveDisk(src, dest)
		towersOfHanoiMove(number-1, aux, src, dest)

def moveDisk(src, dest):
	print(f"move from {src} to {dest}")

if __name__=="__main__":
	towersOfHanoiMove(5, "Source", "Auxiliary", "Destination")