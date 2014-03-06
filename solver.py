import argparse, copy
from scrambler import move, createScrambledPuzzle #Our function

"""
g costo para llegar desde el inicio hasta el actual
h estimado para terminar
"""

def manhattanDistance(puzzle):
	size = len(puzzle)

	mDistance = 0

	for x in range(size):
		for y in range(size):
			if puzzle[x][y] == '@':
				pass
			else:
				col = puzzle[x][y] % size

				aux = int(puzzle[x][y] / size)

				row = ( aux - 1 ) if col == 0 else aux
				
				col = ( col - 1 ) if col != 0 else ( size - 1 ) #Si es multiplo, debe estar en el ultimo lugar

				mDistance += abs(x - row) + abs(y - col)
	return mDistance

def createNode(puzzle, g, blankPosition):
	h = manhattanDistance(puzzle)
	return {
		'puzzle': puzzle,
		'blank': blankPosition,
		'g': g,
		'h': h,
		'f': g + h,
		'parent': None
	}

def findSuccessor(node):
	successors = []
	size = len(node['puzzle'])

	if node['blank']['x'] != 0:
		aux = copy.deepcopy(node['puzzle'])
		b = copy.deepcopy(node['blank'])
		move(aux, size, b, 'up')
		successors.append(createNode(aux, node['g'] + 1, b))

	if node['blank']['x'] != (size - 1):
		aux = copy.deepcopy(node['puzzle'])
		b = copy.deepcopy(node['blank'])
		move(aux, size, b, 'down')
		successors.append(createNode(aux, node['g'] + 1, b))

	if node['blank']['y'] != 0:
		aux = copy.deepcopy(node['puzzle'])
		b = copy.deepcopy(node['blank'])
		move(aux, size, b, 'left')
		successors.append(createNode(aux, node['g'] + 1, b))

	if node['blank']['y'] != size - 1:
		aux = copy.deepcopy(node['puzzle'])
		b = copy.deepcopy(node['blank'])
		move(aux, size, b, 'right')
		successors.append(createNode(aux, node['g'] + 1, b))


	return successors

def equalsPuzzle(fPuzzle, sPuzzle):
	fMan = manhattanDistance(fPuzzle)
	sMan = manhattanDistance(sPuzzle)

	if fMan == 0 and sMan == 0:
		return True
	if fMan != sMan:
		return False
	else:
		for x in range(len(fPuzzle)):
			for y in range(len(fPuzzle)):
				if fPuzzle[x][y] != sPuzzle[x][y]:
					return False

		return True

parser = argparse.ArgumentParser(description='Clasificar elementos basados en un trainer')
parser.add_argument('-s', '--s', dest='size', action='store', required=True, help='The size of the puzzle')
parser.add_argument('-n', '--n', dest='runs', action='store', required=True, help='The number of moves')

args = parser.parse_args()

size = int(args.size)
runs = int(args.runs)

blankPosition, goal, current = createScrambledPuzzle(size, runs)

print 'Puzzle Scrambled'

openList = []
closedList = []
currentNode = None
currentIndex = -1
currentCost = 0 #cost counter

goalNode = createNode(goal, 0, { 'x': size - 1, 'y': size - 1}) #Revisar
openList.append(createNode(current, 0, blankPosition))

while len(openList) != 0:
	for i, x in enumerate(openList):
		if currentNode is None:
			currentNode = x
			currentIndex = i
		else:
			if currentNode['f'] > x['f' ]:
				currentNode = x
				currentIndex = i

	if equalsPuzzle(currentNode['puzzle'], goalNode['puzzle']):

		break #en current node esta la solucion

	currentCost += 1
	successors = findSuccessor(currentNode)

	toRemove = []

	for x in successors:
		removed = False
		append = True
		for y in openList:
			if equalsPuzzle(x['puzzle'], y['puzzle']):
				if x['f'] >= y['f']:
					append = False
					removed = True
					toRemove.append(x)
				else:
					openList.remove(y)
		
		if not removed:
			for y in closedList:
				if equalsPuzzle(x['puzzle'], y['puzzle']):
					append = False
					if x['f'] >= y['f']:
						toRemove.append(x)
					else: 
						closedList.remove(y)

		if append:
			x['parent'] = currentNode
			openList.append(x)

	for x in toRemove:
		successors.remove(x)
	
	openList.remove(currentNode)

	closedList.append(currentNode)
	currentNode = None


aux = [currentNode]
now = currentNode['parent']

while now is not None:
	aux.append(now)
	now = now['parent']

aux.reverse()

for x in aux:
	for y in x['puzzle']:
		print y
	print ""





