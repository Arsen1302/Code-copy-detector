class Solution:
    def solution_1439_3_1(self, bombs: List[List[int]]) -> int:
        
        def solution_1439_3_2(graph, node, been):
            for i in range(len(graph[node])):
                if (graph[node][i]) not in been:
                    been.add(graph[node][i])
                    solution_1439_3_2(graph, graph[node][i], been)


        if len(bombs) == 0: return 0
        # l = length between 2 centers
        d = {} # d = graph | nodes = centers(x,y) | node A is connected(can reach) with node B if A has a radius bigger or equal with the distance between the 2 points 
        for i in range(len(bombs)):
            d[i] = []
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                l = math.sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2) # distance between 2 points
                if l <= bombs[i][2]: # you can reach node J from node I
                    d[i].append(j)
                if l <= bombs[j][2]: # you can reach node I from node J
                    d[j].append(i)
        max_bombs = 1 # if len(bombs) > 0 at least 1 bomb explodes
        for i, element in enumerate(d):
            been = set()
            been.add(element)
            solution_1439_3_2(d, element, been)
            if len(been) == len(bombs): # special case when the all bombs explode | no need to search more
                return len(been)
            max_bombs = max(max_bombs, len(been))
        return max_bombs