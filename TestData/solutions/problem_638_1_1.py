class Solution:
    def solution_638_1_1(self, cells: List[int], N: int) -> List[int]:
        def solution_638_1_2(cells):
            next_day_cells = [0] *len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]: 
                        next_day_cells[i] = 1
                else:
                        next_day_cells[i] = 0
            return next_day_cells
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = solution_638_1_2(cells)

        return cells