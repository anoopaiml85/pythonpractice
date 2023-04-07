class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printlist(self):
        current_head=self.head
        while(current_head):
            if current_head.next == None:
                print("[", current_head.data, "] ", "[", hex(id(current_head)), "]->", "nil")
            else:
                print("[", current_head.data, "] ", "[", hex(
                id(current_head)), "]->", hex(id(current_head.next)))
            current_head = current_head.next
    def insertAfter(self,prev_node,new_data):
        #Check if the previous node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return
        #Create a new node
        new_node= Node(new_data)
        #Make next of new node as next of prev_node
        new_node.next = prev_node.next
        #Make next of prev_node as new_node
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        #if the linklist if empty then make the new node as head. 
        if self.head is None:
            self.head=new_node
            return
        #else traverse till the last node.
        last = self.head
        while(last.next):
            last=last.next
        last.next = new_node    

if __name__=='__main__':
    lst = LinkedList()
    lst.push(2)
    lst.push(3)
    lst.push(5)
    lst.push(7)
    lst.insertAfter(lst.head, 8)
    lst.append(10)
    lst.printlist()
    
