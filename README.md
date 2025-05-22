# Pacman AI — UC Berkeley CS188 Project 1

This repository contains an AI implementation for the classic Pacman game, based on the **UC Berkeley CS188: Intro to Artificial Intelligence** course, specifically [Project 1: Search](https://inst.eecs.berkeley.edu/~cs188/fa24/projects/proj1/). The implementation follows the search algorithms described in lectures and applies them to guide Pacman in solving maze navigation problems.

![image](https://github.com/user-attachments/assets/d8cdb824-e3f1-4811-860d-34d681a11077)

## 📚 Project Overview

Pacman explores mazes using various uninformed and informed search strategies. The goal is to implement core AI search algorithms such as:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

These algorithms are used to solve different game scenarios such as finding a path to a goal, visiting all corners, or collecting all food.

The framework and project description come from the [Berkeley Pacman AI Projects](https://inst.eecs.berkeley.edu/~cs188/fa24/projects/proj1/#q2-3-pts-breadth-first-search-lecture-2), and this implementation is inspired by the repository [Fabioaugustmp/pacman-ai](https://github.com/Fabioaugustmp/pacman-ai).

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pacman-ai.git
cd pacman-ai
````

### 2. Set up the environment

The project requires **Python 3.6+** (no external packages are required).

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Run the Pacman AI

Use the following command format:

```bash
python pacman.py -l [layout] -p [agent] -a [agent-args]
```

### Examples

Run BFS on a simple layout:

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

Use A\* Search with a heuristic:

```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic
```

## 🧠 Implemented Algorithms

You will implement the following algorithms in `search.py`:

* `depthFirstSearch(problem)`
* `breadthFirstSearch(problem)`
* `uniformCostSearch(problem)`
* `aStarSearch(problem, heuristic)`

You’ll also write problem-specific agents in `searchAgents.py`.

## 📁 Repository Structure

```text
pacman-ai/
│
├── pacman.py               # Main game engine
├── search.py               # Search algorithm implementations
├── searchAgents.py         # AI agents using the search algorithms
├── game.py                 # Game logic
├── ghostAgents.py          # (Optional) Ghost agent logic
├── util.py                 # Utility functions (stack, queue, priority queue)
├── layouts/                # Maze layouts
│   └── *.lay               # Text-based layout files
├── test_cases/             # Test cases for automatic grading
├── README.md               # This file
```

## ✅ Project Tasks

Each question in the project adds a new challenge. Here's a checklist:

* [x] Q1: Depth-First Search
* [x] Q2: Breadth-First Search
* [x] Q3: Uniform Cost Search
* [x] Q4: A\* Search
* [ ] Q5+: Corner Search, Food Search (Optional)

See the [official instructions](https://inst.eecs.berkeley.edu/~cs188/fa24/projects/proj1/#q2-3-pts-breadth-first-search-lecture-2) for more details.

## 📷 Screenshots

*BFS in action on mediumMaze:*

![BFS Pacman](docs/bfs_pacman.gif)

## 👨‍🏫 Academic Honor Code

This project is part of the academic curriculum at UC Berkeley. If you are a student, **do not plagiarize** or post your solutions publicly until after the deadline. This repository is for educational and personal learning purposes only.

## 🧑‍💻 Credits

* Project base code by [UC Berkeley CS188](https://inst.eecs.berkeley.edu/~cs188/)
* Original reference repository: [Fabioaugustmp/pacman-ai](https://github.com/Fabioaugustmp/pacman-ai)
