class Solution:
	def solution_487_3(self, graph: List[List[int]]) -> List[List[int]]:
		n = len(graph)
		stack = [[0]]
		paths = []
		while stack: 
			path = stack.pop()
			vertex = path[-1]
			if vertex == n-1:
				paths.append(path.copy())
			for nodes in graph[vertex]:
				stack.append( path.copy()+[nodes])
		return paths