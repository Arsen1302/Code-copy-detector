class Solution:
    def solution_792_2_1(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        disc = discovery time of each node in the graph
        _____________________
        |The concept of 'LOW'|
        low values means to which scc this node belongs to and that if this node is reachable to
        its ancestor (basically is there any way ,  if yes then we assign the low value of this node to the low value of its ancestor which will signify that this node belongs to the SCC and that the edge from this node to the ancestor node is the back edge
        when this node will backtrack to its parent node then it will say that look the connection between you(Parent) and me(child) is not a critical connection because I can be dicovered without your help(Parent) and we all belong to one SCC hence we update the parents low value to the min of low[parent],low[child])
        Next imp thing : 
        _____________________________________________
        |Condition to check if this edge is a bridge | 
        
        eg : SCC1 -----> SCC2
            disc=0       disc =1
            low=0        low=1
        SCC1 =      1->2->3->1           SCC2= 4->5->4
             disc   0  1  2  0           disc   3  4  3
             low    0  0  0  0           low    3  3  3
             
        suppose there s an edge from 1 to 4 and we start our solution_792_2_2 from node 1 then we know that 
        the discovery of node 1 is done before the discovery of node 4 
        now we cant simply compare the dicovery time of the nodes(thats not correct)
        hence we use the low value of the chid to check 
        ___________________________________
        | if dicovery[parent] < low[child] |
        MEANS , That the dicovery ofthe parent was done before that of child hence its value is small if the edge is critical edge 
        else if this edge is not a critical edge then the low value of the child is lesser than or equal to parent
        '''
        disc = [-1]*n
        low = [-1]*n
        self.time = 0
        graph = defaultdict(list)
        bridges = []
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def solution_792_2_2(node,parent):
            #print(parent)
            if disc[node] != -1:
                return 
            
            disc[node] = self.time
            low[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                solution_792_2_2(neighbor,node)
                
                low[node] = min(low[neighbor],low[node])
                
                if disc[node] < low[neighbor] :
                    bridges.append([node,neighbor])
                    
        solution_792_2_2(0,-1)
        #print(low)
        return bridges