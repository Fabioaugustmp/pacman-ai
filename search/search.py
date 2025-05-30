# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from sys import exec_prefix

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        print("Pass here")
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    explored = set()

    node = {'state': problem.getStartState(), 'cost': 0, 'action': None, 'parent': None}
    if problem.isGoalState(node['state']):
        return []

    # print(f"First node: {node}")
    stack.push(node)

    while not stack.isEmpty():
        node = stack.pop()
        # print(f"Node in loop {node}")

        if node['state'] in explored:
            # print(f"{node['state']} is already explored")
            continue

        if node['state'] not in explored:
            # print(f"Adding node {node['state']}")
            explored.add(node['state'])

            successors = problem.getSuccessors(node['state'])
            # print(f"Successors: {successors}")

            for successor, action, stepCost in successors:
                child = {
                    'state': successor,
                    'action': action,
                    'cost': stepCost,
                    'parent': node
                }

                # print(f"Child: {successor}")
                if child['state'] not in explored:
                    if problem.isGoalState(child['state']):
                        # print(f"Found goal state: [ {child} ]")
                        actions = []
                        current_node = child
                        while current_node['parent'] is not None and current_node['action'] is not None:
                            actions.append(current_node['action'])
                            current_node = current_node['parent']

                        actions.reverse()
                        # print(f"Actions: {actions} of the goal state: {actions}")
                        return actions

                    stack.push(child)

        # print(f"Explored so far: {explored}")

    return []
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    node = {'state': problem.getStartState(), 'cost': 0}
    if problem.isGoalState(node['state']):
        return []

    frontier = util.Queue()
    frontier.push(node)

    explored = set()

    while True:
        if frontier.isEmpty():
            raise Exception('Search failed.')

        node = frontier.pop()
        explored.add(node['state'])
        successors = problem.getSuccessors(node['state'])
        for successor in successors:
            child = {'state': successor[0], 'action': successor[1], 'cost': successor[2], 'parent': node}

            if child['state'] not in explored:
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:
                        actions.append(node['action'])
                        node = node['parent']
                    actions.reverse()
                    return actions

                frontier.push(child)

    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
