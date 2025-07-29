class Solution:
	def solution_138_5(self, n):

		squares = [i * i for i in range(1, int(n**0.5)+1)]

		Q = set()
		Q.add((0,0))
		while Q:
			newQ = set()
			for rank, vertex in Q:
				for sq in squares:
					if vertex+sq == n: return rank+1
					newQ.add( (rank+1, vertex+sq) )
			Q = newQ