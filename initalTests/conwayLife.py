import random, time, copy

WIDTH = 60 
HEIGHT = 20

# Create a list of list for the cells:

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living Cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCell is a list of column lists.
    
while True:
    print('\n\n\n\n\n') # Seperate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    
    # Print currentCells on the screen
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
        
    # Calculate the next steps's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get nieghboring coordates
            # WIDTH ensure leftCoord is always between 0 and WIDTH -1 
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y -1) % HEIGHT
            belowCoord = (y +1) % HEIGHT
            
            # Count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
                
            # Set cell based on rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cell with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cell with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(1)