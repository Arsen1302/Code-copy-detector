class Solution:
    def solution_1724_4_1(self, roads, seats):
        graph = defaultdict(set)
        # find the adjacency list representation
        for i,j in roads:
            graph[i].add(j)
            graph[j].add(i)
        n = len(graph)
        if n==0: return 0
        visited = [False]*n
        self.ans = 0
        def solution_1724_4_2(city): 
        # return total number of representatives can be at city
        # and update answer self.ans for each city
            visited[city] = True
            repnum = 1 # initialize with 1 representative of city
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    repnum += solution_1724_4_2(neighbor)
            if city==0: return None # do not update answer for capital
            self.ans += math.ceil(repnum/seats) # update answer
            return repnum
        solution_1724_4_2(0) # execute the DFS
        return self.ans