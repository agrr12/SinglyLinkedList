from node import Node

class SLL_Recursive:
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


    #RECURSIVE-VERSION OF FUNCTIONS


    def printListRecursive(self, current_node):
        if(current_node==None):
            print("") #to skip a line for operations following
            return
        else:
            print(current_node.valueGetter(), end=" ", flush=True)
            return self.printListRecursive(current_node.nextNodeGetter())

    def InsertAtEndRecursive(self, new_value, current_node):
        if self.isEmpty():
            self.InsertAtHead(new_value)
            return
        elif current_node.nextNodeGetter()==None:
            new_node = Node(new_value)
            current_node.nextNodeSetter(new_node)
            return
        else:
            return self.InsertAtEndRecursive(new_value, current_node.nextNodeGetter())

    def InsertAtIndexRecursive(self, new_value, index, current_node):
        if index > 0 and not(current_node==None): #invalid index case
            print("The index inputed is invalid.")
        elif self.isEmpty() or index==0:
            self.InsertAtHead(new_value)
        elif index==1:
            new_node = Node(new_value)
            new_node.nextNodeSetter(current_node.nextNodeGetter()) #Next of new_node is the the next of the current_node
            current_node.nextNodeSetter(new_node)
        else:
            next_index = index-1
            next_node = current_node.nextNodeGetter()
            return self.InsertAtIndexRecursive(new_value, next_index, next_node)

    def DeleteLastRecursive(self, current_node):
        if self.isEmpty():
            return
        next_node = current_node.nextNodeGetter()
        if next_node==None:
            self.head = None
        elif next_node.nextNodeGetter()==None:
            current_node.nextNodeSetter(None)
        else:
            return self.DeleteLastRecursive(next_node)

    def SearchRecursive(self, value_searched, current_node):
        if current_node == None:
            return False
        elif current_node.valueGetter() == value_searched:
            return True
        else:
            next_node = current_node.nextNodeGetter()
            return self.SearchRecursive(value_searched, next_node)

    def DeleteIndexRecursive(self, index, current_node):
        if current_node==None or current_node.nextNodeGetter()==None: #invalid index case
            print("The index inputed is invalid.")
        elif self.isEmpty():
            return
        elif index==0:
            self.DeleteAtHead()
        elif index==1:
            removed_node = current_node.nextNodeGetter()
            next_to_removed = removed_node.nextNodeGetter()
            current_node.nextNodeSetter(next_to_removed)
            removed_node.nextNodeSetter(None)
        else:
            next_node = current_node.nextNodeGetter()
            next_index = index-1
            return self.DeleteIndexRecursive(next_index, next_node)

    def ReturnLastNodeRecursive(self, current_node):
        if current_node==None:
            return None
        elif current_node.nextNodeGetter()==None:
            return current_node
        else:
            next_node = current_node.nextNodeGetter()
            return self.ReturnLastNodeRecursive(next_node)

    def ReverseListRecursive(self, head):
        last_node = self.ReturnLastNodeRecursive(head)
        if head.valueGetter() == last_node.valueGetter():
            return
        else:
            new_first = head.nextNodeGetter()
            head.nextNodeSetter(new_first.nextNodeGetter())
            new_first.nextNodeSetter(self.head)
            self.head = new_first
            return self.ReverseListRecursive(head)



















if __name__ == '__main__':
    s = SLL_Recursive()
    s.printListIterative()
    s.InsertAtHead(2)
    s.InsertAtHead(3)
    s.InsertAtHead(4)
    s.InsertAtHead(5)
    s.InsertAtHead(6)
    s.InsertAtHead(7)
    s.InsertAtHead(8)

    print(s.head.valueGetter())

    s.printListRecursive(s.head)
    s.ReverseListRecursive(s.head)
    s.printListRecursive(s.head)



