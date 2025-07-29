class Solution:
    def solution_1182_3_1(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visited = set()
        res = []
        
        for a, b in adjacentPairs:
            adjList[a].append(b)
            adjList[b].append(a)
            
        def solution_1182_3_2(element):
            visited.add(element)
            res.append(element)
            for nei in adjList[element]:
                if nei not in visited:
                    solution_1182_3_2(nei)
        
        for start in adjList.keys():
            if len(adjList[start]) == 1:
                solution_1182_3_2(start)
                break
        
        return res