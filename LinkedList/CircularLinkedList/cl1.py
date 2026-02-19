class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insersion_at_last(self,val):
        newNode=Node(val)
        if self.head == None:
            self.head=newNode
            newNode.addr=newNode
        else:
            temp=self.head
            while temp.addr!=self.head:
                temp=temp.addr
            newNode.addr=self.head
            temp.addr=newNode
    
    def insersion_at_first(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.addr=newNode
        else:
            temp=self.head
            while temp.addr != self.head:
                temp=temp.addr
            temp.addr=newNode
            newNode.addr=self.head
            self.head=newNode
    
    def insert_at_pos(self,val,idx):
        if idx<=0:
            print('Enter idx greter than 0')
        elif idx>self.length():
            print(f'Enter the idx less than {self.length()}')
        elif idx==1:
            self.insersion_at_first(val)
        elif idx==self.length():
            self.insersion_at_last(val)
        else:
            newNode=Node(val)
            temp=self.head
            cnt=1
            while temp.addr != self.head and cnt<idx-1:
                temp=temp.addr
                cnt+=1
            newNode.addr=temp.addr
            temp.addr=newNode

    def length(self):
        if self.head is None:
            print('Circular Linked List is Empty')
        else:
            cnt=0
            temp=self.head
            while temp:
                cnt+=1
                temp=temp.addr
                if temp==self.head:
                    break
            return cnt
    
    def delete_at_last(self):
        if self.head is None:
            print(f'No element to remove.')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            cnt=1
            while temp.addr != self.head and cnt < self.length()-1:
                cnt+=1
                temp=temp.addr
            temp.addr=self.head
    
    def delete_at_first(self):
        if self.head is None:
            print('No element to remove ')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            while temp.addr != self.head:
                temp=temp.addr
            temp.addr=self.head.addr
            self.head=self.head.addr
    
    def delete_at_pos(self,idx):
        if idx==0 or idx>self.length():
            print(f'Enter id between 1 and {self.length}')
        elif idx==1:
            self.delete_at_first()
        elif idx ==self.length():
            self.delete_at_last()
        else:
            temp=self.head
            cnt=1
            while temp.addr != self.head and cnt+1<idx:
                temp=temp.addr
                cnt+=1
            temp.addr=temp.addr.addr

            
        
    def display(self):
        if self.head is None:
            print('Circular Linked List is Empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' -> ')
                temp=temp.addr
                if temp==self.head:
                    break
            print()


cl1=CircularLinkedList()
while True:
    print('1. Insert at first\n2. Insert at last\n3. Insert at specific position\n4. Length\n5. Display\n6. Delete at first \n7. Delete at last\n8. Delete at specific Position')
    opt=int(input('Enter the option : '))
    match opt:
        case 1:
            val=input('Enter the value : ')
            cl1.insersion_at_first(val)
        case 2:
            val=input('Enter the value : ')
            cl1.insersion_at_last(val)
        case 3:
            val=input('Enter the value : ')
            idx=int(input('Enter the idx : '))
            cl1.insert_at_pos(val,idx)
        case 4:
            cl1.length()
        case 5:
            cl1.display()
        case 6:
            cl1.delete_at_first()
        case 7:
            cl1.delete_at_last()
        case 8:
            idx=int(input('Enter idx : '))
            cl1.delete_at_pos()
        case _:
            print('Invalid input ')
            exit()

