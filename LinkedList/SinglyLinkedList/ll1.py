class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None

class Singly_Linked_List:
    def __init__(self):
        self.head=None

    def insersion_at_last(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            temp=self.head
            while temp.addr:
                temp=temp.addr
            temp.addr=newnode

    def display(self):
        if self.head is None:
            print('Linkedlist is Empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,end=',')
                temp=temp.addr
        print()
    
    def length(self):
        count=0
        if self.head == None:
            print('Length of Linkedlist is 0')
        else:
            temp=self.head
            while temp:
                count+=1
                temp=temp.addr
        return count
   
s1=Singly_Linked_List()
s1.insersion_at_last(1)
s1.insersion_at_last(2)
s1.insersion_at_last(3)
s1.insersion_at_last(4)
s1.display()
print(s1.length())