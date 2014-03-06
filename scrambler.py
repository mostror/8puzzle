import random, argparse, copy

def move(puzzle, size, blankPosition, direction):
	if direction == 'up':

		if blankPosition['x'] == 0: #Esta arriba
			return False
		else:
			aux = puzzle[blankPosition['x'] - 1][blankPosition['y']]

			puzzle[blankPosition['x']][blankPosition['y']] = aux
			puzzle[blankPosition['x'] - 1][blankPosition['y']] = '@'

			blankPosition['x'] -= 1

		return True
	elif direction == 'left':
		if blankPosition['y'] == 0: #Esta a la izquierda
			return False
		else:
			aux = puzzle[blankPosition['x']][blankPosition['y'] - 1]

			puzzle[blankPosition['x']][blankPosition['y']] = aux
			puzzle[blankPosition['x']][blankPosition['y'] - 1] = '@'

			blankPosition['y'] -= 1

		return True
	elif direction == 'right':
		if blankPosition['y'] == ( size - 1 ): #Esta a la derecha
			return False
		else:
			aux = puzzle[blankPosition['x']][blankPosition['y'] + 1]

			puzzle[blankPosition['x']][blankPosition['y']] = aux
			puzzle[blankPosition['x']][blankPosition['y'] + 1] = '@'

			blankPosition['y'] += 1

		return True
	elif direction == 'down':

		if blankPosition['x'] == ( size - 1 ): #Esta abajo
			return False
		else:
			aux = puzzle[blankPosition['x'] + 1][blankPosition['y']]

			puzzle[blankPosition['x']][blankPosition['y']] = aux
			puzzle[blankPosition['x'] + 1][blankPosition['y']] = '@'

			blankPosition['x'] += 1

		return True
	else:
		print 'Wrong move friendo'
		return False

def scramble(puzzle, size, runs, blankPosition):
	x = runs

	directions = ['up', 'down', 'left', 'right']

	while x != 0:
		if move(puzzle, size, blankPosition, directions[random.randint(0, 3)]) is True:
			x -= 1
	
	return puzzle



def createScrambledPuzzle(size, runs):

	blankPosition = {
		'x': ( size - 1 ),
		'y': ( size - 1 )
	}

	puzzle = []

	for x in range(size):
		puzzle.append([])
		for y in range(size):

			if x == size - 1 and y == size - 1:
				puzzle[x].append('@')
			else:
				puzzle[x].append( y + (x * size) + 1 )


	scrambled = scramble(copy.deepcopy(puzzle), size, runs, blankPosition)

	return (blankPosition, puzzle, scrambled)