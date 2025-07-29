class Solution:
    def solution_733_2(self, matrix: List[List[int]]) -> int:
        d = {}
        for row in matrix:
            if row[0] == 0:
                d[tuple(row)] = d.get(tuple(row),0)+1
            else:
                x = []
                for i in row:
                    if i == 0:
                        x.append(1)
                    else:
                        x.append(0)
                d[tuple(x)] = d.get(tuple(x),0)+1
        return max(d.values())