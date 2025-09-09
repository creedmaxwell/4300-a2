from domains.eightpuzzle import Puzzle
from search_core import a_star
import argparse

def print_solution(final_node, stats, algorithm, heuristic):
    if not final_node:
        print("No solution found!")
        return

    print("Domain: 8-Puzzle | Algorithm: " + algorithm.upper())
    if(heuristic == "h0"):
        print("Heuristic: UCS baseline")
    if(heuristic == "h1"):
        print("Heuristic: Misplaced Tiles")
    if(heuristic == "h2"):
        print("Heuristic: Manhattan Distance")
    print(f"Solution cost: {stats.solution_cost} | Depth: {stats.solution_depth}")
    print(f"Nodes generated: {stats.nodes_generated} | Nodes expanded: {stats.nodes_expanded} | Max frontier: {stats.max_frontier}")
    #print("Path:")

    # Reconstruct path
    #path = []
    #current = final_node
    #while current:
    #    path.append((current.state, current.action))
    #    current = current.parent
    #path.reverse()

    # Print initial state
    #print_state(path[0][0])
    
    # Print moves and resulting states
    #for i, (state, action) in enumerate(path[1:], 1):
    #    print(f"\nMove {i}: {action}")
    #    print_state(state)

def print_state(state):
    """Pretty print the 8-puzzle state"""
    for row in state:
        print(" ".join(str(x) if x != 0 else '_' for x in row))

def main():
    parser = argparse.ArgumentParser(description='Run search algorithms on domains')
    parser.add_argument('--domain', choices=['8puzzle'], default='8puzzle', help='Domain to solve')
    parser.add_argument('--h', choices=['h0','h1','h2'], default='h0', help='Heuristic to use')
    parser.add_argument('--algo', choices=['astar'], default='astar', help='Algorithm to use')
    args = parser.parse_args()

    if args.domain == '8puzzle':
        puzzle = Puzzle()
        if args.algo == 'astar':
            solution, stats = a_star(puzzle, puzzle.InitialState(), args.h)
            print_solution(solution, stats, args.algo, args.h)
    else:
        print(f"Domain {args.domain} not implemented")

if __name__ == "__main__":
    main()