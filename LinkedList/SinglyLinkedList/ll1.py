class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None

class Singly_Linked_List:
    def __init__(self):
        self.head=None

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
    
    def insersion_at_last(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            temp=self.head
            while temp.addr:
                temp=temp.addr
            temp.addr=newnode
    def insersion_at_first(self,val):
        temp=Node(val)
        temp.addr=self.head
        self.head=temp

    def insersion_at_posion(self,pos,val):
        if pos>self.length():
            print('Enter posion in range of ->',self.length())
        elif pos<0:
            print('Enter position above 0')
        elif pos==1:
            self.insersion_at_first(val)
        elif pos==self.length()+1:
            self.insersion_at_last(val)
        else:
            newnode=Node(val)
            cnt=0
            temp=self.head
            while temp and cnt-1==pos:
                temp=temp.addr
                cnt+=1
            newnode.addr=temp.addr
            temp.addr=newnode
            
    def delete_at_last(self):
        if self.head==None:
            print('No element to delete')
        else:
            cnt=0
            temp=self.head
            while cnt!=self.length()-2:
                temp=temp.addr
                cnt+=1
            temp.addr=None  
    
    def delete_at_first(self):
        if self.head is None:
            print('No element to delete')
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            head=temp.addr

    def delete_at_index(self,idx):
        if self.head is None:
            print('No nodes to remove')
        elif idx<=0:
            print('Enter index greter than 0')
        elif idx>self.length():
            print('Enter index smaller than -> ',self.length())
        elif idx==1:
            self.delete_at_first()
        elif idx==self.length():
            self.delete_at_last()
        else:
            cnt=1
            temp=self.head
            while cnt<idx-1:
                cnt+=1
                temp=temp.addr
            temp.addr=temp.addr.addr
                


s1=Singly_Linked_List()
print('--------------Singly linkedList Operations ---------------')
while True:
    print('1. Insert at last\n2. Insert at first\n3. Insert at location\n4. Display\n5. Length\n6.Delete at last\n7. Delete at First\n8. Delete at location')
    opt=int(input('Enter the Options'))
    match opt:
        case 1:
            val=input('Enter the Value')
            s1.insersion_at_last(val)
        case 2:
            val=input('Enter the Value')
            s1.insersion_at_first(val)
        case 3:
            val=input('Enter the value ')
            idx=int(input('Enter the index'))
            s1.insersion_at_posion(idx,val)
        case 4:
            s1.display()
        case 5:
            s1.length()
        case 6:
            s1.delete_at_last()
        case 7:
            s1.delete_at_first()
        case 8:
            idx=int(input('Enter the index '))
            s1.delete_at_index(idx)
        case _:
            print('Invalid Index')
            exit()




