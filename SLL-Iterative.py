from node import Node

class SLL_Iterative:
    def __init__(self):
        self.head = None #head é um node


    #GENERAL FUNTIONS

    def headGetter(self):
        return self.head

    def headSetter(self, new_head):
        self.head = new_head

    def isEmpty(self):
        return self.head==None

    def InsertAtHead(self, new_value):
        current_head = self.head
        new_head = Node(new_value)
        new_head.nextNodeSetter(current_head)
        self.head = new_head

    def DeleteAtHead(self):
        if self.isEmpty():
            return
        new_head = self.head.nextNodeGetter()
        self.head.nextNodeSetter(None)
        self.head = new_head

    def printListIterative(self):
        if (self.isEmpty()):
            print("Empty list.")
        else:
            current_node = self.head
            while not (current_node == None):
                print(current_node.valueGetter(), end=" ", flush=True)
                current_node = current_node.nextNodeGetter()
            print("")

    def InsertAtEndIterative(self, new_value):
        if self.isEmpty():
            self.InsertAtHead(new_value)
        else:
            current_node = self.head
            while not (current_node.nextNodeGetter() == None):
                current_node = current_node.nextNodeGetter()
            new_node = Node(new_value)
            current_node.nextNodeSetter(new_node)

    def InsertAtIndexIterative(self, new_value, index):
        if self.isEmpty() or index == 0:
            self.InsertAtHead(new_value)
        else:
            current_node = self.head
            while index > 1:
                if current_node == None:  # If the index is bigger than the list, the loop runs out of nodes before the index reaches 1
                    print("The index inputed is invalid.")
                    return
                current_node = current_node.nextNodeGetter()
                index -= 1
            new_node = Node(new_value)
            new_node.nextNodeSetter(
                current_node.nextNodeGetter())  # Next of new_node is the the next of the current_node
            current_node.nextNodeSetter(new_node)

    def DeleteLastIterative(self):
        if self.isEmpty():
            return

        current_node = self.head
        next_node = current_node.nextNodeGetter()
        if next_node == None:  # The list only has 1 node
            self.head = None
        else:
            while not (next_node.nextNodeGetter() == None):
                current_node = current_node.nextNodeGetter()
                next_node = current_node.nextNodeGetter()
            current_node.nextNodeSetter(None)

    def SearchIterative(self, value_searched):
        if self.isEmpty():
            return False
        else:
            current_node = self.head
            while not (current_node == None):
                if current_node.valueGetter() == value_searched:
                    return True
                else:
                    current_node = current_node.nextNodeGetter()
            return False

    def DeleteIndexIterative(self, index):
        if self.isEmpty():
            return

        if index == 0:
            self.DeleteAtHead()
        else:
            current_node = self.head
            while not (index == 1):
                if current_node == None:
                    break
                current_node = current_node.nextNodeGetter()
                index -= 1
            if current_node == None:
                print("The inputed index is invalid")  # Index bigger than the list
                return
            else:
                removed_node = current_node.nextNodeGetter()
                next_to_removed = removed_node.nextNodeGetter()
                current_node.nextNodeSetter(next_to_removed)
                removed_node.nextNodeSetter(None)

    def ReturnLastNodeIterative(self):
        if self.isEmpty():
            return None
        current_node = self.head
        while not(current_node.nextNodeGetter()==None):
            current_node=current_node.nextNodeGetter()
        return current_node

    def ReverseListIterative(self):
        last_node = self.ReturnLastNodeIterative()
        old_first = self.head
        while not(last_node==old_first):
            next_node = old_first.nextNodeGetter()
            old_first.nextNodeSetter(next_node.nextNodeGetter())
            next_node.nextNodeSetter(self.head)
            self.head = next_node
            last_node = self.ReturnLastNodeIterative()


if __name__ == '__main__':
    s1 = SLL_Iterative()
    s1.InsertAtEndIterative(1)
    s1.InsertAtEndIterative(2)
    s1.InsertAtEndIterative(3)
    s1.InsertAtEndIterative(4)
    s1.printListIterative()
    s1.ReverseListIterative()
    s1.printListIterative()

