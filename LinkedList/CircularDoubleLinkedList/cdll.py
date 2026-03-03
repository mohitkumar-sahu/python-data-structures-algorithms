class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_last(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.next=newNode
            newNode.prev=newNode
        else:
            temp =self.head
            while temp != self.head:
                pass

    def display(self):
        if self.head is None:
            print('No element in C.D.L.L')
        else:
            temp=self.head
            while temp != self.head:
                print(temp.data,end='<=>')

cdll=CircularDoubleLinkedList()
cdll.display()


    
