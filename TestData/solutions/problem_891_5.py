class Solution:
    def solution_891_5(self, arr: List[int]) -> int:
        
        n = len(arr)
        visited = set()
        
        
        if n <= 1:
            return 0
        
        same_value = dict()
        
        for i, v in enumerate(arr):
            if v not in same_value.keys():
                same_value[v]= [i]
            else:
                same_value[v].append(i)
                
        stack = list()
        level = 0
        
        stack.append((0,0))
        total = -1
        
        
        while stack:
            level,node = stack.pop(0)
        
            visited.add(node)
            
            if node == n-1:
                return level
            else:
                for a in same_value[arr[node]] :
                    if a != node and a not in visited:
                        stack.append((level+1,a))
                
                same_value[arr[node]].clear()
                
                if node+1 < n and node+1 not in visited:
                    stack.append((level+1,node+1))
                 
                if node-1 >=0 and node-1 not in visited:
                    stack.append((level+1,node-1))
                    

                                 
        return level