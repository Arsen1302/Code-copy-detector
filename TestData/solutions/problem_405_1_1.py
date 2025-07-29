class Solution:
    def solution_405_1_1(self, n: int, k: int, row0: int, col0: int) -> float:
	
		# precalculate possible moves
        adj_list = defaultdict(list)
        d = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))
        for row in range(n):
            for col in range(n):
                for dx, dy in d:
                    pos = (row + dx, col + dy)
                    if 0 <= pos[0] < n and 0 <= pos[1] < n:
                        adj_list[(row, col)].append(pos)

        @cache
        def solution_405_1_2(pos, h):
            if h == k:
                return 1
            
            res = 0
            for next_pos in adj_list[pos]:
                res += solution_405_1_2(next_pos, h + 1)
                
            return res            
            
        leafs_num = solution_405_1_2((row0, col0), 0)

        return leafs_num / 8**k