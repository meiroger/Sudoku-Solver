import copy

class Stack:
    def __init__(self, initialContents = []):
        self.theStack = initialContents[:]

    def __str__(self):
        return "The stack contains: " + str(self.theStack)
    
    def isEmpty(self):
        return len(self.theStack) == 0

    def push(self, elt):
        self.theStack.append(elt)

    def pop(self):
        """delete and return the last item in the list."""
        x = self.theStack[len(self.theStack)-1]
        del self.theStack[len(self.theStack)-1]
        return x     
    
class Queue:
    def __init__(self, initialContents = []):
        self.theQueue = initialContents[:]

    def __str__(self):
        return "The queue contains: " + str(self.theQueue)
    
    def isEmpty(self):
        return len(self.theQueue) == 0

    def push(self, elt):
        self.theQueue.append(elt)

    def pop(self):
        x = self.theQueue[0]
        del self.theQueue[0]
        return x


class board:
    """The board class represents a state (situation) in a sudoku puzzle. Some
    cells may have been defined numbers while others have not."""
    
    def __init__(self):
        self.num_nums_placed = 0
        self.size = 9
        self.rows = []
        for i in range(self.size):
            row = []
            for j in range(self.size):    
                row.append(range(1,self.size+1)) #range creates a list of 1-9
            self.rows.append(row)

    def findMostConstrainedCell(self):
        row = 0
        col = 0
        minimum = 10
        for r in range(9):
            therow = self.rows[r]
            for c in range(9):
                thecell = self.rows[r][c]
                if (isinstance(thecell,list)) and (len(thecell) < minimum):
                    minimum = len(thecell)
                    row = r
                    col = c
        return (row,col)

    def __str__(self):
        s = "num_nums_placed: " + str(self.num_nums_placed) + "\n"
        s += str(self.rows)
        return s

    def printPretty(self):
        """prints all numbers assigned to cells (in self.rows). If a cell
        has not been assigned (that is, it is a list), then print 0, to indicate
        not yet assigned. """
        print "num_nums_placed is: " + str(self.num_nums_placed)
        for i in self.rows:
            for x in i:
                if isinstance(x,list):
                    print 0,
                else:
                    print x,
            print 

    def failureTest(self):
        """returns true if we find any cells that are [], false if none are found."""
        for i in self.rows:
            for x in i:
                if (x == []):
                    return True
        return False

    def goalTest(self):
        """returns true if there are 81 numbers placed, false otherwise """
        """for i in self.rows:
            for x in i:
                if isinstance(x,list):
                    return False
        return True"""
        if (self.num_nums_placed == 81):
            return True
        else:
            return False

    def update(self, row, column, assignment):
        newstate = copy.deepcopy(self)
        newstate.num_nums_placed += 1
        newstate.rows
        newstate.rows[row][column] = assignment
        b1 = [0,1,2]
        b2 = [3,4,5]
        b3 = [6,7,8]
        # removing assignment as a possibility from the lists
        if (row in b1):
            if (column in b1): # quadrant 1
                for i in b1:
                    temprow = newstate.rows[i]
                    for j in b1:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b2): # quadrant 2
                for i in b1:
                    temprow = newstate.rows[i]
                    for j in b2:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b3): # quadrant 3
                for i in b1:
                    temprow = newstate.rows[i]
                    for j in b3:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)

        if (row in b2):
            if (column in b1): # quadrant 4
                for i in b2:
                    temprow = newstate.rows[i]
                    for j in b1:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b2): # quadrant 5
                for i in b2:
                    temprow = newstate.rows[i]
                    for j in b2:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b3): # quadrant 6
                for i in b2:
                    temprow = newstate.rows[i]
                    for j in b3:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)

        if (row in b3):
            if (column in b1): # quadrant 7
                for i in b3:
                    temprow = newstate.rows[i]
                    for j in b1:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b2): # quadrant 8
                for i in b3:
                    temprow = newstate.rows[i]
                    for j in b2:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
            if (column in b3): # quadrant 9
                for i in b3:
                    temprow = newstate.rows[i]
                    for j in b3:
                        tempcolumn = temprow[j]
                        if (isinstance(tempcolumn,list)) and (assignment in tempcolumn):
                            tempcolumn.remove(assignment)
                
        for r in range(9):
            tempcell = newstate.rows[r][column]
            if (isinstance(tempcell,list)) and (assignment in tempcell):
                tempcell.remove(assignment)
        for col in range(9):
            tempcell = newstate.rows[row][col]
            if (isinstance(tempcell,list)) and (assignment in tempcell):
                tempcell.remove(assignment)
        return newstate
        
    
def DFS(state):
    # make a stack
    theStack = Stack()
    # step 1 adding initial state (root) to the list
    theStack.push(state)
    # step 2: choosing a node (curr) to examine from the list
    #      if there is nothing in list, then failure test returns true
    while (not theStack.isEmpty()):
        curr = theStack.pop()
    # step 3: checking if the current board is a goal state
        if curr.goalTest():   
            return curr          #if so, SOLUTION 
        else:                    #if not, continue
            if (not curr.failureTest()):
                (row,col) = curr.findMostConstrainedCell()
                curr.rows[row][col]
                for assignment in curr.rows[row][col]:
                    theStack.push(curr.update(row,col,assignment))
    # step 4: expanding curr by applying all possible operations
    #    add the new states to the list

    #step 5: go to step 2

def BFS(state):
    theQueue = Queue()
    theQueue.push(state)
    while (not theQueue.isEmpty()):
        curr = theQueue.pop()
        if curr.goalTest():  
            return curr          #if so, SOLUTION 
        else:                    #if not, continue
            if (not curr.failureTest()):
                (row,col) = curr.findMostConstrainedCell()
                curr.rows[row][col]
                for assignment in curr.rows[row][col]:
                    theQueue.push(curr.update(row,col,assignment))
                    
# Example Sudoku Boards:

b = board()
b = b.update(0, 1, 7)
b = b.update(0, 7, 1)
b = b.update(1, 2, 9)
b = b.update(1, 3, 7)
b = b.update(1, 5, 4)
b = b.update(1, 6, 2)
b = b.update(2, 2, 8)
b = b.update(2, 3, 9)
b = b.update(2, 6, 3)
b = b.update(3, 1, 4)
b = b.update(3, 2, 3)
b = b.update(3, 4, 6)
b = b.update(4, 1, 9)
b = b.update(4, 3, 1)
b = b.update(4, 5, 8)
b = b.update(4, 7, 7)
b = b.update(5, 4, 2)
b = b.update(5, 6, 1)
b = b.update(5, 7, 5)
b = b.update(6, 2, 4)
b = b.update(6, 5, 5)
b = b.update(6, 6, 7)
b = b.update(7, 2, 7)
b = b.update(7, 3, 4)
b = b.update(7, 5, 1)
b = b.update(7, 6, 9)
b = b.update(8, 1, 3)
b = b.update(8, 7, 8)
b.printPretty()
solution = DFS(b)
print solution

b = board()
b = b.update(0, 1, 2)
b = b.update(0, 3, 3)
b = b.update(0, 5, 5)
b = b.update(0, 7, 4)
b = b.update(1, 6, 9)
b = b.update(2, 1, 7)
b = b.update(2, 4, 4)
b = b.update(2, 7, 8)
b = b.update(3, 0, 1)
b = b.update(3, 2, 7)
b = b.update(3, 5, 9)
b = b.update(3, 8, 2)
b = b.update(4, 1, 9)
b = b.update(4, 4, 3)
b = b.update(4, 7, 6)
b = b.update(5, 0, 6)
b = b.update(5, 3, 7)
b = b.update(5, 6, 5)
b = b.update(5, 8, 8)
b = b.update(6, 1, 1)
b = b.update(6, 4, 9)
b = b.update(6, 7, 2)
b = b.update(7, 2, 6)
b = b.update(8, 1, 4)
b = b.update(8, 3, 8)
b = b.update(8, 5, 7)
b = b.update(8, 7, 5)
b.printPretty()
solution = DFS(b)
print solution

b = board()
b = b.update(0, 1, 2)
b = b.update(0, 3, 3)
b = b.update(0, 5, 5)
b = b.update(0, 7, 4)
b = b.update(1, 6, 9)
b = b.update(2, 1, 7)
b = b.update(2, 4, 4)
b = b.update(2, 7, 8)
b = b.update(3, 0, 1)
b = b.update(3, 2, 7)
b = b.update(3, 5, 9)
b = b.update(3, 8, 2)
b = b.update(4, 1, 9)
b = b.update(4, 4, 3)
b = b.update(4, 7, 6)
b = b.update(5, 0, 6)
b = b.update(5, 3, 7)
b = b.update(5, 6, 5)
b = b.update(5, 8, 8)
b = b.update(6, 1, 1)
b = b.update(6, 4, 9)
b = b.update(6, 7, 2)
b = b.update(7, 2, 6)
b = b.update(8, 1, 4)
b = b.update(8, 3, 8)
b = b.update(8, 5, 7)
b = b.update(8, 7, 5)
b.printPretty()
solution = BFS(b)
print solution
