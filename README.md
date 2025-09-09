# 8-Puzzle Solver with A* Search

This project implements an A* search algorithm to solve the 8-puzzle problem using different heuristics.

## Problem Description
The 8-puzzle consists of a 3×3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles from an initial configuration to the goal state where the numbers are in order with the blank in the bottom right.

Goal State:
```
1 2 3
4 5 6
7 8 _
```

## Implementation
- A* search with three heuristic options:
  - h0: No heuristic (equivalent to Uniform Cost Search)
  - h1: Misplaced Tiles heuristic
  - h2: Manhattan Distance heuristic

## Usage
Run the solver with different heuristics:
```bash
python run.py --domain 8puzzle --algo astar --h h0  # UCS baseline
python run.py --domain 8puzzle --algo astar --h h1  # Misplaced tiles
python run.py --domain 8puzzle --algo astar --h h2  # Manhattan distance
```

## Statistics Tracked
- Solution cost and depth
- Number of nodes generated
- Number of nodes expanded
- Maximum frontier size

## File Structure
```
4300-a2/
├── domains/
│   └── eightpuzzle.py    # 8-puzzle problem implementation
├── search_core.py        # A* search implementation
└── run.py               # Main script to run solver
```