class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_last(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp

    def insert_at_first(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def length(self):
        temp=self.head
        cnt=0
        while temp:
            cnt+=1
            temp=temp.next
        return cnt

    def insert_at_pos(self,val,idx):
        if idx<1 or idx>self.length()+1:
            print(f'Enter idx between 1 and {self.length()+1}')
        elif idx==1:
            self.insert_at_first(val)
        elif idx==self.length()+1:
            self.insert_at_last(val)
        else:
            newNode=Node(val)
            temp=self.head
            cnt=0
            while temp is not None and cnt<idx-1:
                temp=temp.next
            newNode.next=temp.next
            newNode.prev=temp
            temp.next=newNode
            temp.next.prev=newNode

    def display(self):
        if self.head is None:
            print('No element in D.L.L')
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' <=> ')
                temp=temp.next
            print()

    def delete_at_last(self):
        if self.head is None:
            print('No element present in D.L.L')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            while temp.next.next != None:
                temp=temp.next
            temp.next.prev=None
            temp.next=None
    
    def delete_at_first(self):
        if self.head is None:
            print('No element present in D.L.L')
        elif self.length()==1:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
    
    def delete_at_pos(self,pos):
        if self.head is None:
            print('No element in D.L.L')
        elif pos<1 or pos>self.length()+1:
            print(f'Enter the position b/w 1 and {self.length()}')
        elif pos==1:
            self.delete_at_first()
        elif pos==self.length():
            self.delete_at_last()
        else:
            temp=self.head
            cnt=1
            while cnt<pos-1:
                temp=temp.next
                cnt+=1
            temp.next=temp.next.next
            if temp.next is not None:
                temp.next.prev=temp


dll=DoublyLinkedList()
# dll.insert_at_last(10)
# dll.insert_at_last(20)
# dll.insert_at_last(30)
# dll.insert_at_first(40)
# dll.insert_at_first(50)
# dll.insert_at_first(60)
dll.insert_at_pos(20,1)
dll.insert_at_pos(30,2)
dll.insert_at_pos(40,3)
dll.display()
# dll.delete_at_last()
# dll.delete_at_last()
# dll.delete_at_last()
# dll.delete_at_first()
# dll.delete_at_first()
# dll.delete_at_first()
dll.delete_at_pos(2)
# dll.insert_at_pos(30,5)
dll.display()

