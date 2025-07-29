class Solution:
	def solution_891_4(self, arr: List[int]) -> int:

		n=len(arr)

		if n<2:
			return 0

		graph={}

		for i in range(n):

			if arr[i] not in graph:
				graph[arr[i]]=[i]

			else:
				graph[arr[i]].append(i)


		current = [0]
		visited = {0}
		step = 0

		while current:

			next=[]

			for node in current:

				if node == n-1:
					return step

				for child in graph[arr[node]]:
					if child not in visited:
						visited.add(child)
						next.append(child)

				graph[arr[node]].clear()
				for child in [node-1 , node+1]:
					if 0<= child <len(arr) and child not in visited:
						visited.add(child)
						next.append(child)

			current = next
			step = step + 1

		return -1
		
# If It is Usefull to Understand Please UpVote  🙏🙏