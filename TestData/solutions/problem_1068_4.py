class Solution:
    def solution_1068_4(self, mat: List[List[int]]) -> int:

        transpose = [list(x) for x in zip(*mat)]
        c = 0
      
        for row in mat:
            if row.count(1) == 1:
                idx = row.index(1)

                if transpose[idx].count(1) == 1:
                    c += 1

        return c