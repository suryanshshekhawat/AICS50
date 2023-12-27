import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    # if we use a DFS implementation we use a Stack frontier

    def __init__(self):
        # initially it is an empty list
        self.frontier = [] 

    def add(self, node):
        # adds node to frontier
        self.frontier.append(node) 

    def contains_state(self, state):
        # checks if given node in frontier
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        # checks if frontier is empty
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # returns the removed node (last in was out)
            # this is a stack.
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1] # remove last node
            return node

class QeueuFrontier(StackFrontier):
    # If we wish to implement BFS, we can use a Queue Frontier
    # For this we inherit methods and constructor from the
    # Stack Frontier except the overridden method of remove.

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            # returns the removed node (first in was out)
            # this is a queue
            node = self.frontier[0]
            self.frontier = self.frontier[1:] # remove first node
            return node
        
class Maze():
    