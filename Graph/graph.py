class Graph:
    def __init__(self):
        self.g1={}
    
    def display(self):
        for k,v in self.g1.items():
            print(k,' : ',v)

    def addVertex(self,vertex):
        if vertex not in self.g1:
            self.g1[vertex]=[]
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.g1 and vertex2 in self.g1:
            self.g1[vertex1].append(vertex2)
            self.g1[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdges(self,vertex1,vertex2):
        if vertex1 in self.g1 and vertex2 in self.g1:
            self.g1[vertex1].remove(vertex2)
            self.g1[vertex2].remove(vertex1)
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex in self.g1:
            for adj_vertex in self.g1[vertex]:
                self.g1[adj_vertex].remove(vertex)
            del self.g1[vertex]
            return True
        return False

o1=Graph()
o1.addVertex('A')
o1.addVertex('B')
o1.addVertex('C')
o1.addVertex('D')
o1.addVertex('E')
o1.addEdge('A','B')
o1.addEdge('A','C')
o1.addEdge('A','D')
o1.addEdge('B','E')
o1.addEdge('D','E')
o1.removeEdges('C','A')
o1.removeVertex('C')
o1.display()
