# Linear Queue with unlimited size

class QUEUE:
    def __init__(self):
        self.q1=[]

    def enqueue(self,val:int):
        self.q1.append(val)

    def dequeue(self):
        print(f"pop element is {self.q1.pop(0)}")

    def peek(self):
        print(f"Peek element is {self.q1[0]}")
    
    def display(self):
        print(self.q1)
    
o1=QUEUE()
o1.enqueue(1)
o1.enqueue(2)
o1.enqueue(3)
o1.enqueue(4)
o1.enqueue(5)
o1.display()
o1.peek()
o1.dequeue()
o1.peek()
o1.display()
    
