# Implimatation of Circular Queue with limited Size.

class CircularQueue:
    def __init__(self,maxSize):
        self.cq=[None]*maxSize
        self.maxSize=maxSize
        self.front=-1
        self.rear=-1

    def display(self):
        print(self.cq)
        print(f'front -> {self.front}')
        print(f'rear -> {self.rear}')

    def IsEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True

    def IsFull(self):
        if self.front==0 and self.rear==self.maxSize-1:
            return True
        elif self.rear + 1 == self.front:
            return True
        else:
            return False
    
    def enqueue(self,val):
        if self.IsFull():
            print('Queue is full')
        else:
            if self.rear+1==self.maxSize:
                self.rear=0
            else:
                self.rear+=1
                if self.front==-1:
                    self.front=0
            self.cq[self.rear]=val
                
    def dequeue(self):
        if self.IsEmpty():
            print('Queue is empty')
        else:
            start=self.front
            if self.front==self.rear:
                self.front=-1
                self.rare=-1
            elif self.front+1==self.maxSize:
                self.front+=1
            else:
                self.front+=1
            self.cq[start]=None



o1=CircularQueue(5)
o1.display()
o1.enqueue(10)
o1.enqueue(20)
o1.enqueue(30)
o1.enqueue(50)
o1.enqueue(60)
o1.display()