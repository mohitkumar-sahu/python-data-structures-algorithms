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
            while temp.next != self.head:
                temp=temp.next
            newNode.next=self.head
            newNode.prev=temp
            temp.next=newNode
            self.head.prev=newNode
    
    def insert_at_first(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.next=newNode
            newNode.prev=newNode
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            newNode.next=self.head
            newNode.prev=temp
            temp.next=newNode
            self.head=newNode


    def display(self):
        if self.head is None:
            print('No element in C.D.L.L')
        else:
            temp=self.head
            while temp:
                print(temp.data,end='<=>')
                temp=temp.next
                if temp==self.head:
                    break
            print()

    def length(self):
        if self.head is None:
            return 0
        else:
            temp=self.head
            cnt=0
            while temp:
                cnt+=1
                temp=temp.next
                if temp==self.head:
                    break
        return cnt
    
    def insert_at_loc(self,val,pos):
        newNode=Node(val)
        if pos<=0 :
            print(f'Enter the pos b/w 1 and {self.length()}')
        elif pos==1:
            self.insert_at_first(val)
        elif pos==self.length()+1:
            self.insert_at_last(val)
        else:
            temp=self.head
            cnt=0
            while temp.next != None and cnt<pos-1:
                temp=temp.next
                cnt+=1
            newNode.prev=temp
            newNode.next=temp.next
            temp.next.prev=newNode
            temp.next=newNode
    
    def delete_at_last(self):
        if self.head is None:
            print('No element in CDLL')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            while temp.next.next != self.head:
                temp=temp.next
            temp.next=self.head
            self.head.prev=temp

    def delete_at_first(self):
        if self.head is None:
            print('No element in CDLL')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=self.head.next
            self.head=temp.next
    
    def delete_at_pos(self,pos):
        if pos<=0:
            print(f'Enter pos b/w 1 and {self.length()}')
        elif pos==1:
            self.delete_at_first()
        elif pos==self.length()+1:
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
    
    def search_the_ele(self,val):
        if self.head is None:
            print('No ele in CDLL')
        else:
            temp=self.head
            while temp:
                if temp.data==val:
                    print(f'{val} Data is found')
                    break
                temp=temp.next
                if temp==self.head:
                    print(val,'Value not found')
                    break
    
    def display_nodes_prev_and_next(self,val):
        prev_data=None
        next_data=None
        if self.head==None:
            print('No ele in CDLL')
        temp=self.head
        while temp:
            if temp.data==val:
                next_data=temp.next.data
                prev_data=temp.prev.data
                break
            temp=temp.next
            if temp==self.head:
                print(f'{val} not present in CDLL ')
                break
        print(f'Previous Data : {prev_data}\nNext Data : {next_data}')

cdll=CircularDoubleLinkedList()
# cdll.insert_at_last(10)
# cdll.insert_at_last(20)
# cdll.insert_at_last(30)
# cdll.insert_at_first(40)
# cdll.insert_at_first(50)
cdll.insert_at_loc(10,1)
cdll.insert_at_loc(20,2)
cdll.insert_at_loc(30,3)
cdll.insert_at_loc(40,4)
cdll.insert_at_loc(50,5)
cdll.display()
# cdll.insert_at_loc(25,2)
# cdll.delete_at_first()
# cdll.delete_at_first()
# cdll.delete_at_first()
# cdll.insert_at_loc(35,2)
# cdll.insert_at_loc(30,3)
# cdll.delete_at_pos(2)
# cdll.delete_at_pos(2)
# print(cdll.length())
cdll.display_nodes_prev_and_next(50)
cdll.display()



    
