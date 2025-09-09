import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g=0, f=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.f = f
        self.depth = 0 if parent is None else parent.depth + 1

class Stats:
    def __init__(self):
        self.nodes_generated = 0
        self.nodes_expanded = 0
        self.max_frontier = 0
        self.solution_cost = 0
        self.solution_depth = 0

def a_star(problem, initial_state, heuristic="h0"):
    stats = Stats()

    h0 = problem.Heuristic(heuristic, initial_state)
    start_node = Node(initial_state, None, None, g=0, f=h0)

    frontier = []
    heapq.heappush(frontier, (start_node.f, id(start_node), start_node))
    frontier_dict = {initial_state: start_node}

    best_g = {initial_state: 0}

    while frontier:
        stats.max_frontier = max(stats.max_frontier, len(frontier))

        current_f, _, n = heapq.heappop(frontier)

        if n.state in frontier_dict:
            if frontier_dict[n.state] != n:
                continue
            del frontier_dict[n.state]

        stats.nodes_expanded += 1

        if problem.GoalTest(n.state):
            stats.solution_cost = n.g
            stats.solution_depth = n.depth
            return n, stats
        
        for action in problem.Actions(n.state):
            stats.nodes_generated += 1
            s_prime = problem.Transition(n.state, action)
            g_prime = n.g + problem.StepCost(n.state, action, s_prime)

            if s_prime not in best_g or g_prime < best_g[s_prime]:
                best_g[s_prime] = g_prime
                f_prime = g_prime + problem.Heuristic(heuristic, s_prime)
                s_node = Node(s_prime, n, action, g_prime, f_prime)

                if s_prime in frontier_dict:
                    old_node = frontier_dict[s_prime]
                    old_node.f = float('inf')
                
                heapq.heappush(frontier, (s_node.f, id(s_node), s_node))
                frontier_dict[s_prime] = s_node
    
    return None, stats
