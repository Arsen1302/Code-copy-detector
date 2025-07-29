class Solution:
    def solution_288_1(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        # group values in matrix by the sum of their indices in a map
        map = {}
        for i in range(len(matrix) + len(matrix[0]) - 1):
            map[i] = []

        # populate the map
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                map[i + j].append(val)

        # iterate through map and reverse values where key is divisible by two
        for k, v in map.items():
            if k % 2 == 0:
                map[k] = v[::-1]
        
        # populate output
        for v in map.values():
            for val in v:
                res.append(val)
                
        return res