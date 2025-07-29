class Solution:
    def solution_616_3_1(self, n: int) -> int:
        Mod = 10**9 + 7
        pad = [
            (4, 6), (8, 6), (7, 9), (4, 8), (3, 9, 0),
            (), (1, 7, 0), (2, 6), (1, 3), (2, 4)
        ]
        
        @cache
        def solution_616_3_2(i, n):
		   # search reached the end, found 1 solution
            if n == 0: return 1
			# search not reach the end, keep looking for solution for n - 1
            return sum(solution_616_3_2(nxt, n - 1) for nxt in pad[i]) % Mod

        # starting from each number, count the total solution to n
		# because placing the chess to i takes 1 count, so search for n - 1
        return sum(solution_616_3_2(i, n - 1)  for i in range(10)) % Mod