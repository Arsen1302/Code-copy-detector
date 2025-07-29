class Solution:
    def solution_1636_3_1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        e = defaultdict(set)
        restricted = set(restricted)
        for ed in edges:

            if ed[1] not in restricted and ed[0] not in restricted:
                e[ed[0]].add(ed[1])
                e[ed[1]].add(ed[0])
                
        

        visited = set()

        def solution_1636_3_2(node):
            if node in visited:
                return 
            
            visited.add(node)
            self.total+=1
            
            for s in e[node]:
                solution_1636_3_2(s)

        
        self.total = 1
        visited.add(0)
        for s in e[0]:
            solution_1636_3_2(s)
        
        return self.total