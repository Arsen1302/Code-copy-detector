class Solution:
	def solution_1629_1_1(self, start: int) -> Dict[int, int]:
		distances = defaultdict(lambda: math.inf)

		queue = deque([start])
		level = 0

		while queue:
			for _ in range(len(queue)):
				curr = queue.popleft()

				if distances[curr] <= level:    
					continue

				distances[curr] = level

				for neighbor in graph[curr]:
					queue.append(neighbor)

			level += 1        

		return distances

    def solution_1629_1_2(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]
        
        for _from, to in enumerate(edges):
            if to != -1:
                graph[_from].append(to)
        
        a = self.solution_1629_1_1(node1)
        b = self.solution_1629_1_1(node2)
                
        options = []    
        
        for idx in range(n):
            if a[idx] != math.inf and b[idx] != math.inf:
                options.append((max(a[idx], b[idx]), idx))
                
        if not options:
            return -1        
        
        return min(options)[1]