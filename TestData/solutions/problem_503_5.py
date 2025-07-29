class Solution:
    def solution_503_5(self, routes: List[List[int]], source: int, target: int) -> int:
        queue = deque([(source, 0)])
        graph = defaultdict(set)
        visited = set()
        
        for routeIdx, route in enumerate(routes):
            for busStop in route:
                graph[busStop].add(routeIdx)
                        
        while queue:
            curStop, curDist = queue.popleft()

            if curStop == target:
                return curDist
            
            visited.add(curStop)
            
            for routeIdx in graph[curStop]:
                for stop in routes[routeIdx]:
                    if stop not in visited:
                        queue.append((stop, curDist + 1))
						
                routes[routeIdx] = set()

        return -1