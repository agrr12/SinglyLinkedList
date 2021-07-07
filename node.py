
#Class that represents a node with two properties: a stored value and a pointer to another node

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    #Getters and Setters
    def valueGetter(self):
        return self.value
    def nextNodeGetter(self):
        return self.nextNode
    def valueSetter(self, newValue):
        self.value = newValue
    def nextNodeSetter(self, newNextNode):
        self.nextNode = newNextNode
