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
player_block_i = -1
player_block_j = -1
player_block_dir = 'None'

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
                node.children[i] = Node.Node()
                node.children[i].array = copy.deepcopy(node.array)
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
    def checkVirtualScore(self, node, val, i, j):
        total_count = 0
        connect = 1
        if val == -1:
            ind = i
            # vertical add
            i += 1
            if i < 6:
                if i + connect <= 6:
                    if node.array[i + connect][j] == val:
                        total_count += 2
                        connect += 1
                        if i + connect <= 6:
                            if node.array[i + connect][j] == val:
                                total_count += 3
                                connect += 1
                                if i + connect <= 6:
                                    if node.array[i + connect][j] == val:
                                        total_count += 995
                                        return total_count
            i = ind
            # horizontalR add
            ind = j
            j += 1
            if j < 6:
                connect = 1
                if j + connect <= 6:
                    if node.array[i][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if j + connect <= 6:
                            if node.array[i][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if j + connect <= 6:
                                    if node.array[i][j + connect] == val:
                                        total_count += 995
                                        return total_count
            j = ind
            # horizontalL add
            ind = j
            j -= 1
            if j > 0:
                connect = 1
                if j + connect >= 0:
                    if node.array[i][j - connect] == val:
                        total_count += 2
                        connect += 1
                        if j + connect >= 0:
                            if node.array[i][j - connect] == val:
                                total_count += 3
                                connect += 1
                                if j + connect >= 0:
                                    if node.array[i][j - connect] == val:
                                        total_count += 995
                                        return total_count
            j = ind
            ind = i
            indj = j
            i += 1
            j += 1
            # HR add
            if j < 6 and i < 6:
                connect = 1
                if i + connect <= 6 and j + connect <= 6:
                    if node.array[i + connect][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if i + connect <= 6 and j + connect <= 6:
                            if node.array[i + connect][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if i + connect <= 6 and j + connect <= 6:
                                    if node.array[i + connect][j + connect] == val:
                                        total_count += 995
                                        return total_count
            i = ind
            j = indj
            # HL add
            ind = i
            indj = j
            i += 1
            j -= 1
            if j < 6 and i > 0:
                connect = 1
                if i - connect <= 6 and j + connect <= 6:
                    if node.array[i - connect][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if i - connect <= 6 and j + connect <= 6:
                            if node.array[i - connect][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if i - connect <= 6 and j + connect <= 6:
                                    if node.array[i - connect][j + connect] == val:
                                        total_count += 995
                                        return total_count

            return total_count
        else:

            if node.array[i][j] != val:
                return 0
            # vertical add
            if i < 6:
                if i + connect <= 6:
                    if node.array[i + connect][j] == val:
                        total_count += 2
                        connect += 1
                        if i + connect <= 6:
                            if node.array[i + connect][j] == val:
                                total_count += 3
                                connect += 1
                                if i + connect <= 6:
                                    if node.array[i + connect][j] == val:
                                        total_count += 995
                                        return total_count

            # horizontalR add
            if j < 6:
                connect = 1
                if j + connect <= 6:
                    if node.array[i][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if j + connect <= 6:
                            if node.array[i][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if j + connect <= 6:
                                    if node.array[i][j + connect] == val:
                                        total_count += 995
                                        return total_count

            # horizontalL add
            if j > 0:
                connect = 1
                if j + connect >= 0:
                    if node.array[i][j - connect] == val:
                        total_count += 2
                        connect += 1
                        if j + connect >= 0:
                            if node.array[i][j - connect] == val:
                                total_count += 3
                                connect += 1
                                if j + connect >= 0:
                                    if node.array[i][j - connect] == val:
                                        total_count += 995
                                        return total_count

            # HR add
            if j < 6 and i < 6:
                connect = 1
                if i + connect <= 6 and j + connect <= 6:
                    if node.array[i + connect][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if i + connect <= 6 and j + connect <= 6:
                            if node.array[i + connect][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if i + connect <= 6 and j + connect <= 6:
                                    if node.array[i + connect][j + connect] == val:
                                        total_count += 995
                                        return total_count

            # HL add
            if j < 6 and i > 0:
                connect = 1
                if i - connect <= 6 and j + connect <= 6:
                    if node.array[i - connect][j + connect] == val:
                        total_count += 2
                        connect += 1
                        if i - connect <= 6 and j + connect <= 6:
                            if node.array[i - connect][j + connect] == val:
                                total_count += 3
                                connect += 1
                                if i - connect <= 6 and j + connect <= 6:
                                    if node.array[i - connect][j + connect] == val:
                                        total_count += 995
                                        return total_count

            return total_count

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

    def calculateStateBestScore(self, node, ind, val):
        array_of_score = [0] * gameSize
        blacklist = [0] * gameSize

        if ind == round(gameSize / 2) - 1:
            for i in range(gameSize):
                if node.array[i][ind] == 1 and array_of_score[ind] == 0:
                    array_of_score[round(gameSize / 2) - 1] = 4

        for i in range(gameSize):
            max_value = 0
            if i not in blacklist:
                for j in range(gameSize):
                    if self.checkVirtualScore(node, val, i, j) != 0:
                        max_value += self.checkVirtualScore(node, val, i, j)
                        if max_value > array_of_score[j]:
                            array_of_score[j] += max_value
                        if array_of_score[j] > max_value and ind == round(gameSize / 2) - 1:
                            array_of_score[j] += max_value
                    else:
                        if node.array[i][j] == -1:
                            array_of_score[j] -= 10
                            blacklist.append(i)
                            continue

        if ind == round(gameSize / 2) - 1:
            for i in range(gameSize):
                if node.array[i][ind] == 1 and array_of_score[ind] == 0:
                    array_of_score[round(gameSize / 2) - 1] = 4

        return array_of_score[ind]

    def checkStateForCPUDecision(self, node, i, val):
        array_of_score = [0] * gameSize
        array_of_enemy = [0] * gameSize
        if node is not None:
            if node.children[0] is None:
                return self.calculateStateBestScore(node, i, val)
            else:
                max_value = 0
                for i in range(gameSize):
                    array_of_score[i] += self.checkStateForCPUDecision(node.children[i], i, 1)
                    array_of_enemy[i] += self.checkStateForCPUDecision(node.children[i], i, -1)
                for j in range(gameSize):
                    if array_of_enemy[j] > 300:
                        array_of_score[j] = -array_of_enemy[j]
                return array_of_score
        return array_of_score

# computer decides what position to play
    def CPU_Decide(self):
        global winner
        best_value = self.checkStateForCPUDecision(self.tree, 0, 0)
        index = 0
        maxV = 0
        for i in range(gameSize):
            if self.root.array[0][i] != 0:
                best_value[i] = 0

        print(best_value)

        for i in range(gameSize):
            if best_value[i] < -300:
                index = i
                break
            if maxV < best_value[i]:
                index = i
                maxV = best_value[i]

        self.gameStatesV(index, self.root)
        if self.checkState(self.root) == 4:
            winner = turn

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