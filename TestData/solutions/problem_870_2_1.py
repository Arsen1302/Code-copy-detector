class Solution:
    def solution_870_2_1(self, n: int, a: List[List[int]]) -> int:
        length = len(a)
        if length < n - 1:
            return -1
        nodes = set()
        connections = defaultdict(list)
        
        for src,dest in a:
            connections[src].append(dest)
            connections[dest].append(src)
        
        def solution_870_2_2(src):
            if src in nodes:
                return
            nodes.add(src)
            for node in connections[src]:
                solution_870_2_2(node)
            
        
        result = 0
        for i in range(n):
            if i not in nodes:
                solution_870_2_2(i)
                result+=1
        
        return result - 1