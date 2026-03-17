# Implementation of Graph using Dictionary

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
    
    #B.F.S Traversing
    def bfs_traversing(self,vertex):
        if vertex in self.g1:
            visited=[vertex]
            queue=[vertex]
            while queue:
                dvertex=queue.pop(0)
                print(dvertex,end=' ')
                for adj_vertex in self.g1[dvertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        queue.append(adj_vertex)


    #D.F.S Traversing
    def dfs_traversing(self,vertex):
        if vertex in self.g1:
            visited=[vertex]
            stack=[vertex]
            while stack:
                dvertex=stack.pop()
                print(dvertex,end=' ')
                for adj_vertex in self.g1[dvertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        stack.append(adj_vertex)

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
# o1.removeEdges('C','A')
# o1.removeVertex('C')
o1.display()
print('BFS Traversing')
o1.bfs_traversing('A')
print()
print('DFS Traversing')
o1.dfs_traversing('A')
