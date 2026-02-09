# Implimetation of stack with unlimited size

class STACK:
    s1=[]
    # def __init__(self):
    #     self.s1=[]

    def push(self,num):
        self.s1.append(num)

    def pop(self):
        self.s1.pop()

    def display(self):
        if len(self.s1)==0:
            print('Stack is empty')
        else:
            print(self.s1)
    
    def peek_ele(self):
        print(self.s1[len(self.s1)-1])

o1=STACK()
o1.display()
o1.push(10)
o1.push(15)
o1.push(20)
o1.push(25)
o1.display()
o1.pop()
o1.display()
o1.peek_ele()