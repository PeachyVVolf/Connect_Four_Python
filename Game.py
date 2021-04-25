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
turn_num = 0

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
            count = 2
        else:
            count = 4
        self.tree = copy.deepcopy(self.root)
        self.createTree(self.tree, count)

    def createTree(self, node, count):
        if difficultyLevel == 'Easy':
            if count > 0:
                for i in range(gameSize):
                    node.children[i] = Node.Node()
                    node.children[i].array = copy.deepcopy(node.array)
                    self.gameStatesV(i, node.children[i])
                    changeVirtualTurn()
                    self.createTree(node.children[i], count-1)
                    changeVirtualTurn()
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
    def checkVirtualScore(self, node, i, j, val):
        if node.array[i][j] == val:
            total_sum = 0
            connect = 1
            # check left
            if j > 0:
                if node.array[i][j - connect] == val:
                    total_sum += 2
                    connect += 1
                    if j - connect >= 0:
                        if node.array[i][j - connect] == val:
                            total_sum += 3
                            connect += 1
                            if j - connect >= 0:
                                if node.array[i][j - connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check right
            if j < 6:
                if node.array[i][j + connect] == val:
                    total_sum += 2
                    connect += 1
                    if j + connect <= 6:
                        if node.array[i][j + connect] == val:
                            total_sum += 3
                            connect += 1
                            if j + connect <= 6:
                                if node.array[i][j + connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check down
            if i < 6:
                if node.array[i + connect][j] == val:
                    total_sum += 2
                    connect += 1
                    if i + connect <= 6:
                        if node.array[i + connect][j] == val:
                            total_sum += 3
                            connect += 1
                            if i + connect <= 6:
                                if node.array[i + connect][j] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check up
            if i > 0:
                if node.array[i - connect][j] == val:
                    total_sum += 2
                    connect += 1
                    if i - connect >= 0:
                        if node.array[i - connect][j] == val:
                            total_sum += 3
                            connect += 1
                            if i - connect >= 0:
                                if node.array[i - connect][j] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check DRD
            if i < 6 and j < 6:
                if node.array[i + connect][j + connect] == val:
                    total_sum += 2
                    connect += 1
                    if i + connect <= 6 and j + connect <= 6:
                        if node.array[i + connect][j + connect] == val:
                            total_sum += 3
                            connect += 1
                            if i + connect <= 6 and j + connect <= 6:
                                if node.array[i + connect][j + connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check DRU
            if i > 0 and j < 6:
                if node.array[i - connect][j + connect] == val:
                    total_sum += 2
                    connect += 1
                    if i - connect >= 0 and j + connect <= 6:
                        if node.array[i - connect][j + connect] == val:
                            total_sum += 3
                            connect += 1
                            if i - connect >= 0 and j + connect <= 6:
                                if node.array[i - connect][j + connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check DLU
            if i > 0 and j > 0:
                if node.array[i - connect][j - connect] == val:
                    total_sum += 2
                    connect += 1
                    if i - connect >= 0 and j - connect >= 0:
                        if node.array[i - connect][j - connect] == val:
                            total_sum += 3
                            connect += 1
                            if i - connect >= 0 and j - connect >= 0:
                                if node.array[i - connect][j - connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1
            # check DLD
            if i < 6 and j > 0:
                if node.array[i + connect][j - connect] == val:
                    total_sum += 2
                    connect += 1
                    if i + connect <= 6 and j - connect >= 0:
                        if node.array[i + connect][j - connect] == val:
                            total_sum += 3
                            connect += 1
                            if i + connect <= 6 and j - connect >= 0:
                                if node.array[i + connect][j - connect] == val:
                                    total_sum += 995
                                    return total_sum
            connect = 1

            return total_sum
        else:
            return 0

    def checkVirtualScoreEnemy(self, node, i, j, val):
        if node.array[i][j] == val:
            total_sum = 0
            connect = 1
            # check left
            if j > 0:
                if node.array[i][j - connect] == val:
                    total_sum -= 2
                    connect += 1
                    if j - connect >= 0:
                        if node.array[i][j - connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check right
            if j < 6:
                if node.array[i][j + connect] == val:
                    total_sum -= 2
                    connect += 1
                    if j + connect <= 6:
                        if node.array[i][j + connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check down
            if i < 6:
                if node.array[i + connect][j] == val:
                    total_sum -= 2
                    connect += 1
                    if i + connect <= 6:
                        if node.array[i + connect][j] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check up
            if i > 0:
                if node.array[i - connect][j] == val:
                    total_sum -= 2
                    connect += 1
                    if i - connect >= 0:
                        if node.array[i - connect][j] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check DRD
            if i < 6 and j < 6:
                if node.array[i + connect][j + connect] == val:
                    total_sum -= 2
                    connect += 1
                    if i + connect <= 6 and j + connect <= 6:
                        if node.array[i + connect][j + connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check DRU
            if i > 0 and j < 6:
                if node.array[i - connect][j + connect] == val:
                    total_sum -= 2
                    connect += 1
                    if i - connect >= 0 and j + connect <= 6:
                        if node.array[i - connect][j + connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check DLU
            if i > 0 and j > 0:
                if node.array[i - connect][j - connect] == val:
                    total_sum -= 2
                    connect += 1
                    if i - connect >= 0 and j - connect >= 0:
                        if node.array[i - connect][j - connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1
            # check DLD
            if i < 6 and j > 0:
                if node.array[i + connect][j - connect] == val:
                    total_sum -= 2
                    connect += 1
                    if i + connect <= 6 and j - connect >= 0:
                        if node.array[i + connect][j - connect] == val:
                            total_sum -= 995
                            return total_sum
            connect = 1

            return total_sum
        else:
            return 0

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

    def calculateStateBestScore(self, node):
        array_of_score = [[0] * gameSize for _ in range(gameSize)]
        sum_of_score = [0] * gameSize

        if virtual_turn == 'max':
            for i in range(gameSize):
                for j in range(gameSize):
                    array_of_score[i][j] = self.checkVirtualScore(node, i, j, 1)

            print(array_of_score[i])
        if virtual_turn == 'min':
            for i in range(gameSize):
                for j in range(gameSize):
                    if self.checkVirtualScoreEnemy(node, i, j, -1) < -300:
                        array_of_score[i][j] = self.checkVirtualScoreEnemy(node, i, j, -1)

            print(array_of_score[i])

        for i in range(gameSize):
            for j in range(gameSize):
                sum_of_score[j] += array_of_score[i][j]

        return sum_of_score

    def checkStateForCPUDecision(self, node):
        # changeVirtualTurn()
        array_of_score = [0] * gameSize
        if node is not None:
            if node.children[0] is None:
                someValue = self.calculateStateBestScore(node)
                print(virtual_turn)
                if virtual_turn == 'min':
                    print(min(someValue))
                    changeVirtualTurn()
                    return min(someValue)
                else:
                    print(max(someValue))
                    changeVirtualTurn()
                    return max(someValue)
            else:
                max_value = 0
                for i in range(gameSize):
                    array_of_score[i] = self.checkStateForCPUDecision(node.children[i])

                print(array_of_score)
                print(virtual_turn)
                if virtual_turn == 'min':
                    print(min(array_of_score), array_of_score.index(min(array_of_score)))
                    return min(array_of_score), array_of_score.index(min(array_of_score))
                else:
                    print(max(array_of_score), array_of_score.index(max(array_of_score)))
                    return max(array_of_score), array_of_score.index(max(array_of_score))

# computer decides what position to play
    def CPU_Decide(self):
        global turn_num
        global winner
        global virtual_turn
        index = -1
        virtual_turn = 'min'
        best_value = self.checkStateForCPUDecision(self.tree)
        index = best_value[1]
        if turn_num == 0:
            index = 3
            turn_num += 1
        print(index, best_value)
        self.gameStatesV(index, self.root)
        print(self.root.array)
        if self.checkState(self.root) == 4:
            winner = turn
            self.endgame()

# computer play function
    def gameStates(self):
        global winner
        row = 0
        col = 3
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
                self.endgame()

        changeTurn()
        self.createTreeForDif()
        #self.gameStates()
        self.CPU_Decide()
        changeTurn()
        self.createGUI()
        return

    def gamePlay(self):
        self.createTreeForDif()
        self.CPU_Decide()
        changeTurn()
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
        global player_block_j
        global player_block_i
        global player_block_dir
        maxV = 0
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if node.array[i][j] == val:
                    count += 1
                    if count > maxV:
                        maxV = count
                        if maxV == 3:
                            player_block_j = j
                            player_block_i = i
                            player_block_dir = 'Hor'
                    if count == 4:
                        return count
                else:
                    count = 0

        return maxV

    def checkVertical(self, node, val):
        global player_block_j
        global player_block_i
        global player_block_dir
        maxV = 0
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if node.array[j][i] == val:
                    count += 1
                    if count > maxV:
                        maxV = count
                        if maxV == 3:
                            player_block_j = j
                            player_block_i = i
                            player_block_dir = 'Ver'
                    if count == 4:
                        return count
                else:
                    count = 0

        return maxV

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