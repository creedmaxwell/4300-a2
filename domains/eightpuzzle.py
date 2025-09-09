class Puzzle:
    def __init__(self):
        self.goal_state = ((1,2,3),
                           (4,5,6),
                           (7,8,0))
        
    def InitialState(self):
        return ((7,2,4),
                (5,0,6),
                (8,3,1))

    def Actions(self, state):
        actions = []
        blank_row, blank_col = None, None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    blank_row, blank_col = i, j
                    break
        
        possible_moves = [
            ('up', (-1, 0)),
            ('down', (1,0)),
            ('left', (0,-1)),
            ('right', (0,1))
        ]

        for move, (dr, dc) in possible_moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                actions.append(move)
        
        return actions

    def Transition(self, state, action):
        blank_row, blank_col = None, None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    blank_row, blank_col = i, j
                    break
        
        moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        dr, dc = moves[action]
        new_row, new_col = blank_row + dr, blank_col + dc

        new_state = [list(row) for row in state]
        
        new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]

        return tuple(tuple(row) for row in new_state)

    def GoalTest(self, state):
        return state == self.goal_state

    def StepCost(self, state, action, next_state):
        return 1
    
    def MisplacedTiles(self, state):
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
                    count +=1
        return count
    
    def ManhattanDistance(self, state):
        distance = 0
        goal_positions = {}
        for i in range(3):
            for j in range(3):
                if self.goal_state[i][j] != 0:
                    goal_positions[self.goal_state[i][j]] = (i,j)

        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i, goal_j = goal_positions[state[i][j]]
                    distance += abs(i - goal_i) + abs(j- goal_j)
        
        return distance

    def Heuristic(self, heuristic, state):
        if heuristic == "h0":
            return 0
            # UCS baseline
        if heuristic == "h1":
            return self.MisplacedTiles(state)
        if heuristic == "h2":
            return self.ManhattanDistance(state)

    