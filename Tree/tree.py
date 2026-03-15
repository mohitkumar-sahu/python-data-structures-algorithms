class Tree:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
    
    def Insert_at_ele(self,val):
        if self.data:
            if val<self.data:
                if self.prev is None:
                    self.prev=Tree(val)
                else:
                    self.prev.Insert_at_ele(val)
            elif val>self.data:
                if self.next is None:
                    self.next=Tree(val)
                else:
                    self.next.Insert_at_ele(val)

    def display(self):
        if self.prev:
            self.prev.display()
        print(self.data,end='->')
        if self.next:
            self.next.display()
    
    def pre_order_traversal(self,root):
        if root:
            print(root.data,end='->')
            self.pre_order_traversal(root.prev)
            self.pre_order_traversal(root.next)

    def in_order_traversal(self,root):
        if root:
            self.in_order_traversal(root.prev)
            print(root.data,end='->')
            self.in_order_traversal(root.next)
    
    def post_order_traversal(self,root):
        if root:
            self.post_order_traversal(root.prev)
            self.post_order_traversal(root.next)
            print(root.data,end='->')
    
    def Level_order(self,root):
        if root:
            print(root.data,end='->')
            self.Level_order(root.prev)
            self.Level_order(root.next)
        
c1=Tree(15)
c1.Insert_at_ele(10)
c1.Insert_at_ele(20)
c1.Insert_at_ele(7)
c1.Insert_at_ele(14)
c1.Insert_at_ele(19)
c1.Insert_at_ele(28)
c1.Insert_at_ele(4)
c1.Insert_at_ele(9)
c1.display()
print()
print('Pre order Traversal')
print(c1.pre_order_traversal(c1))
print()
print('In order Traversal')
print(c1.in_order_traversal(c1))
print()
print('Post order Traversal')
print(c1.post_order_traversal(c1))
print()
print('Level order Traversal')
print(c1.Level_order(c1))