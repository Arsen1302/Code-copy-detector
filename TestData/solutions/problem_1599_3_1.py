class Solution:
    def solution_1599_3_1(self, n: int, edges: List[List[int]]) -> int:
        
        graph=[]
        for i in range(n):
            graph.append([])
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
                
        visited=[0]*n
        
        def solution_1599_3_2(graph,i,visited):
            if graph[i]==[]:
                return 
            for neigh in graph[i]:
                if not visited[neigh]:
                    visited[neigh]=1
                    self.count+=1
                    solution_1599_3_2(graph,neigh,visited)
                    
        tot=0
        prev=0           
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                self.count=1
                solution_1599_3_2(graph,i,visited)
                tot+=prev*self.count
                prev+=self.count
                
        
        return tot