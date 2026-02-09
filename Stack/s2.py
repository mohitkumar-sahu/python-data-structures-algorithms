# Implimetation of stack with limited size

class STACK:
    def __init__(self,stacksize: int):
        self.s1=[]
        self.stacksize=stacksize
    
    def IsFull(self):
        if len(self.s1)==self.stacksize:
            return True
        else:
            return False
    
    def IsEmpty(self):
        if len(self.s1)==0:
            return True
        else :
            return False
    
    def display(self):
        if self.IsEmpty():
            print('Stck is Empty')
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
    
    def push(self,val):
        if self.IsFull():
            print('Stack is Full')
        else:
            self.s1.append(val)
    
    def pop(self):
        if self.IsEmpty():
            print('Stack is Empty')
        else:
            print(f'Pop item is {self.s1.pop()}')
    
    def peek(self):
        if self.IsEmpty():
            pass
        else:
            print(f'Peek element is {self.s1[-1]}')
    
o1=STACK(4)
while True:
    print('----------Stack Operations---------------')
    print('1.push\n2.pop\npeek\n3.display\n4Isfull\n5IsEmpty')
    opt=int(input('Enter the opertions : '))
    match opt:
        case 1:
            val=int(input('Enter the element'))
            o1.push(val)
        case 2:
            o1.pop()
        case 3:
            o1.peek()
        case 4:
            o1.IsFull()
        case 5:
            o1.IsEmpty()

            
        