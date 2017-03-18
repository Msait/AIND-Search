import logging

logging.basicConfig(level=logging.INFO)

def solution(node):
    logging.debug("Current node state (%s, %s)" % (node.getState()))
    path = [node.getAction()]
    if node.getParent() is None:
        return []
    l = solution(node.getParent())
    return path + l

def test_node_contains(list, searchState):
    for (priority, node) in list:
        if (node.getState() == searchState): return node
        else: return None

def replace_frontier_with_lowest_cost(node, with_node):
    node = with_node
    # updated_queue = [with_node if n.getState() == node.getState() else n for n in priority_queue.heap]
    # priority_queue.heap = updated_queue


def calculateTotalPathCost(node):
    if node.getParent() is None:
        return node.getCost()
    else:
        return node.getCost() + calculateTotalPathCost(node.getParent())

class Node:
    def __init__(self, parent, state, action, cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.totalPathCost = calculateTotalPathCost(self)

    def getTotalPathCost(self):
        return self.totalPathCost

    def getState(self):
        return self.state

    def getCost(self):
        return self.cost

    def getAction(self):
        return self.action

    def getParent(self):
        return self.parent

    def solution(self):
        result = []
        if self.parent is None:
            return result
        else:
            result = solution(self)
            result.reverse()
            return result

    def __str__(self):
        return "Node[ State: {}, cost: {}, action: {}, parent: {}".format(self.state, self.cost, self.action, self.parent)
