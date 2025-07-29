class Solution:
	def solution_1091_2(self, n: int, roads: List[List[int]]) -> int:
		if roads == []: #egde case check
			return 0

		node_degrees = defaultdict(int)
		for i in roads:
			node_degrees[i[0]]+=1
			node_degrees[i[1]]+=1

		maxx1, maxx2 = 0, 0
		ans = 0
		for i, k in node_degrees.items():      #O(N)
			if k >= maxx1:
				maxx1 = k
				maxx2 = 0
				for j, l in node_degrees.items():       #O(N)
					if l >= maxx2 and j!=i:
						maxx2 = l
						if [i, j] in roads or [j, i] in roads:           #O(N)
							ans = max(ans, maxx1 + maxx2 - 1)
						else:
							ans = max(ans, maxx1 + maxx2 )
		return ans