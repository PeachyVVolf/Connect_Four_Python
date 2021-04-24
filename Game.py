import random
import Node
import tkinter
import copy

top = tkinter.Tk()
top.title("Connect Four")

gameSize = 7
difficultyLevel = 'Easy'
winner = 'None'
turn = 'max'
virtual_turn = 'max'
CPU_best_count = 0
CPU_best_index_i = -1
CPU_best_index_j = -1
CPU_Direction = 'None'
Player_best_count = 0
Player_best_index_i = -1
Player_best_index_j = -1
Player_Direction = 'None'
childIndex = -1

# changes global turn variable
def changeTurn():
    global turn
    if turn == 'min':
        turn = 'max'
    elif turn == 'max':
        turn = 'min'

def changeVirtualTurn():
    global virtual_turn
    if virtual_turn == 'min':
        virtual_turn = 'max'
    elif virtual_turn == 'max':
        virtual_turn = 'min'


class Game:
    button = [[None] * gameSize for _ in range(gameSize)]

    def __init__(self):
        self.root = Node.Node()
        self.tree = None

# create tree
    def createTreeForDif(self):
        global virtual_turn
        virtual_turn = turn
        if difficultyLevel == 'Easy':
            count = 0
        else:
            count = 4
        self.tree = copy.deepcopy(self.root)
        self.createTree(self.tree, count)

    def createTree(self, node, count):
        if difficultyLevel == 'Easy':
            for i in range(gameSize):
                node.children[i] = copy.deepcopy(node)
                self.gameStatesV(i, node.children[i])
        elif difficultyLevel == 'Hard':
            if count > 0:
                for i in range(gameSize):
                    node.children[i] = Node.Node()
                    node.children[i].array = copy.deepcopy(node.array)
                    self.gameStatesV(i, node.children[i])
                    changeVirtualTurn()
                    self.createTree(node.children[i], count-1)
                    changeVirtualTurn()
            else:
                return

# set the value of specified player in array as 1 for CPU and -1 for player
    def playerTurn(self, node, row, col, val):
        node.setValue(row, col, val)

# computer play with value passed
    def checkVirtualHorizontal(self, node, val):
        global CPU_best_count
        global CPU_best_index_i
        global CPU_best_index_j
        global CPU_Direction
        global Player_best_count
        global Player_best_index_i
        global Player_best_index_j
        global Player_Direction
        count = 0
        for i in range(gameSize):
            for j in range(gameSize):
                if node.array[i][j] == val:
                    count += 1
                    if val == -1:
                        if count > Player_best_count:
                            Player_best_count = count
                            Player_best_index_i = i
                            Player_best_index_j = j
                            Player_Direction = 'Hor'
                    elif val == 1:
                        if count > CPU_best_count:
                            CPU_best_count = count
                            CPU_best_index_i = i
                            CPU_best_index_j = j
                            CPU_Direction = 'Hor'
                else:
                    count = 0

    def checkVirtualVirtical(self, node, val):
        global CPU_best_count
        global CPU_best_index_i
        global CPU_best_index_j
        global CPU_Direction
        global Player_best_count
        global Player_best_index_i
        global Player_best_index_j
        global Player_Direction
        count = 0
        for i in range(gameSize):
            for j in range(gameSize):
                if node.array[j][i] == val:
                    count += 1
                    if val == -1:
                        if count > Player_best_count:
                            Player_best_count = count
                            Player_best_index_i = j
                            Player_best_index_j = i
                            Player_Direction = 'Ver'
                    elif val == 1:
                        if count > CPU_best_count:
                            CPU_best_count = count
                            CPU_best_index_i = j
                            CPU_best_index_j = i
                            CPU_Direction = 'Ver'
                else:
                    count = 0

    def checkVirtualDL(self, node, val):
        global CPU_best_count
        global CPU_best_index_i
        global CPU_best_index_j
        global CPU_Direction
        global Player_best_count
        global Player_best_index_i
        global Player_best_index_j
        global Player_Direction
        count = 0
        row = 0
        col = 0
        for i in range(gameSize):
            for j in range(gameSize):
                if node.array[row][col] == val:
                    count += 1
                    row += 1
                    col -= 1
                    if val == -1:
                        if count > Player_best_count:
                            Player_best_count = count
                            Player_best_index_i = i
                            Player_best_index_j = j
                            Player_Direction = 'DL'
                    elif val == 1:
                        if count > CPU_best_count:
                            CPU_best_count = count
                            CPU_best_index_i = i
                            CPU_best_index_j = j
                            CPU_Direction = 'DL'
                else:
                    count = 0

    def checkVirtualDR(self, node, val):
        global CPU_best_count
        global CPU_best_index_i
        global CPU_best_index_j
        global CPU_Direction
        global Player_best_count
        global Player_best_index_i
        global Player_best_index_j
        global Player_Direction
        count = 0
        row = 0
        col = 0
        for i in range(gameSize):
            for j in range(gameSize):
                if node.array[row][col] == val:
                    count += 1
                    row += 1
                    col += 1
                    if val == -1:
                        if count > Player_best_count:
                            Player_best_count = count
                            Player_best_index_i = i
                            Player_best_index_j = j
                            Player_Direction = 'DR'
                    elif val == 1:
                        if count > CPU_best_count:
                            CPU_best_count = count
                            CPU_best_index_i = i
                            CPU_best_index_j = j
                            CPU_Direction = 'DR'
                else:
                    count = 0

    def gameStatesV(self, col, node):
        row = 0
        if virtual_turn == 'max':
            val = 1
        else:
            val = -1

        while node.array[row][col] == 0 and row < gameSize - 1:
            row += 1
        if node.array[row][col] != 0:
            row -= 1
        self.playerTurn(node, row, col, val)

        return

    def blockPlayer(self):
        row = 0
        col = childIndex
        while self.root.array[row][col] == 0 and row < gameSize - 1:
            row += 1
        if self.root.array[row][col] != 0:
            row -= 1
        self.playerTurn(self.root, row, col, 1)

    def completeAndWin(self, node):
        global winner
        self.findBestPath()
        winner = 'max'
        print('YOU LOST!!')
        self.createGUIWithoutButton()
        return

    def findBestPath(self):
        if CPU_Direction == 'Hor':
            for i in range(CPU_best_count):
                if self.tree.array[CPU_best_index_i][CPU_best_index_j - i] == 0:
                    self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_j - i].array)
                    return
                elif self.tree.array[CPU_best_index_i][CPU_best_index_j + i] == 0:
                    self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_j + i].array)
                    return
        if CPU_Direction == 'Ver':
            if self.tree.array[CPU_best_index_i - CPU_best_count][CPU_best_index_j] == 0:
                self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_j].array)
            else:
                self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_j + 1].array)
        if CPU_Direction == 'DL':
            if self.tree.array[CPU_best_index_i - CPU_best_count][CPU_best_index_j + CPU_best_count] == 0:
                self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_i - CPU_best_count].array)
        if CPU_Direction == 'DR':
            if self.tree.array[CPU_best_index_i - CPU_best_count][CPU_best_index_j - CPU_best_count] == 0:
                self.root.array = copy.deepcopy(self.tree.children[CPU_best_index_i - CPU_best_count].array)

    def checkStateForCPUDecision(self):
        global CPU_best_count
        global Player_best_count
        global childIndex

        maxyet = -1
        if difficultyLevel == 'Easy':
            for i in range(gameSize):
                self.checkVirtualHorizontal(self.tree.children[i], -1)
                self.checkVirtualHorizontal(self.tree.children[i], 1)
                self.checkVirtualVirtical(self.tree.children[i], -1)
                self.checkVirtualVirtical(self.tree.children[i], 1)
                self.checkVirtualDL(self.tree.children[i], -1)
                self.checkVirtualDL(self.tree.children[i], 1)
                self.checkVirtualDR(self.tree.children[i], -1)
                self.checkVirtualDR(self.tree.children[i], 1)

                if maxyet < CPU_best_count:
                    maxyet = CPU_best_count
                    childIndex = i

                if CPU_best_count == 3:
                    childIndex = CPU_best_index_j
                    self.completeAndWin(self.tree.children[childIndex])
                elif CPU_best_count < 4 and Player_best_count == 3:

                    childIndex = Player_best_index_j
                    self.blockPlayer()
                    return
                elif i == gameSize - 1:

                    self.findBestPath()
                    return

# computer decides what position to play
    def CPU_Decide(self):
        self.checkStateForCPUDecision()

# computer play function
    def gameStates(self):
        global winner
        row = 0
        col = random.randrange(gameSize)
        while self.root.array[row][col] == 0 and row < gameSize - 1:
            row += 1
        if self.root.array[row][col] != 0:
            row -= 1
        self.playerTurn(self.root, row, col, 1)
        if self.checkState(self.root) == 4:
            winner = turn

        changeTurn()
        return

# player play function
    def onButtonPress(self, i, j):
        global winner
        i = 0
        if turn == 'min':
            while self.root.array[i][j] == 0 and i < gameSize - 1:
                i += 1
            if self.root.array[i][j] != 0:
                i -= 1
            self.playerTurn(self.root, i, j, -1)

            if self.checkState(self.root) == 4:
                winner = turn

        changeTurn()
        self.createTreeForDif()
        #self.gameStates()
        self.CPU_Decide()
        changeTurn()
        self.createGUI()
        return

    def gamePlay(self):
        global winner
        self.gameStates()
        self.createGUI()

# functions to check whether a win state has been reached
    def checkDiagonalR(self, node, i, j, val):
        row = i
        col = j
        count = 0
        for k in range(4):
            if row < gameSize and col < gameSize:
                if node.array[row][col] == val:
                    count += 1
                    row += 1
                    col += 1
                    if count == 4:
                        return count
                else:
                    return 0

        return count

    def checkDiagonalL(self, node, i, j, val):
        row = i
        col = j
        count = 0
        for k in range(4):
            if row < gameSize and col < gameSize:
                if node.array[row][col] == val:
                    count += 1
                    row -= 1
                    col += 1
                    if count == 4:
                        return count
                else:
                    return 0

        return count

    def checkHorizontal(self, node, val):
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if node.array[i][j] == val:
                    count += 1
                    if count == 4:
                        return count
                else:
                    count = 0

        return count

    def checkVertical(self, node, val):
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if node.array[j][i] == val:
                    count += 1
                    if count == 4:
                        return count
                else:
                    count = 0

        return count

    def checkState(self, node):
        count = 0
        if turn == 'max':
            # check horizontally
            count = self.checkHorizontal(node, 1)
            if count == 4:
                return count
            # check vertically
            count = self.checkVertical(node, 1)
            if count == 4:
                return count
            # check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    count = self.checkDiagonalR(node, i, j, 1)
                    if count == 4:
                        return count
            # check diagonally left
            for i in range(gameSize):
                count = 0
                for j in range(gameSize - 1, 0, -1):
                    count = self.checkDiagonalL(node, i, j, 1)
                    if count == 4:
                        return count
        elif turn == 'min':
            ##check horizontally
            count = self.checkHorizontal(node, -1)
            if count == 4:
                return count
            ##check vertically
            count = self.checkVertical(node, -1)
            if count == 4:
                return count
            ##check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    count = self.checkDiagonalR(node, i, j, -1)
                    if count == 4:
                        return count
            ##check diagonally left
            for i in range(gameSize):
                count = 0
                for j in range(gameSize - 1, 0, -1):
                    count = self.checkDiagonalL(node, i, j, -1)
                    if count == 4:
                        return count
        return 0

# assign colour to the tiles
    def colour(self, i, j):
        if self.root.array[i][j] == -1:
            self.button[i][j].config(bg='green')
        elif self.root.array[i][j] == 1:
            self.button[i][j].config(bg='red')
        else:
            self.button[i][j].config(bg='white')

# create GUI with functioning buttons
    def createGUI(self):
        self.endgame()
        for i in range(gameSize):
            for j in range(gameSize):
                self.button[i][j] = tkinter.Button(top, text=self.root.array[i][j], command=lambda row=i, column=j: self.onButtonPress(row, column), width=4, height=3)
                self.colour(i, j)
                self.button[i][j].grid(row=i, column=j)

        top.mainloop()

# create GUI with no functioning buttons as this would be called on game end
    def createGUIWithoutButton(self):
        for i in range(gameSize):
            for j in range(gameSize):
                self.button[i][j] = tkinter.Button(top, text=self.root.array[i][j], width=4, height=3)
                self.colour(i, j)
                self.button[i][j].grid(row=i, column=j)

        top.mainloop()
        return

# end Game
    def endgame(self):
        if winner == 'min':
            print('YOU WON!!')
            self.createGUIWithoutButton()
            return
        elif winner == 'max':
            print('YOU LOST!!')
            self.createGUIWithoutButton()
            return