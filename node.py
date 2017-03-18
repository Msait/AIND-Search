import logging

logging.basicConfig(level=logging.INFO)

def solution(node):
    logging.debug("Current node state (%s, %s)" % (node.getState()))
    path = [node.getAction()]
    if node.getParent() is None:
        return []
    l = solution(node.getParent())
    return path + l


class Node:
    def __init__(self, parent, state, action, cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost

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
