class Solution:
    def solution_737_1_1(self, tiles: str) -> int:
        record = [0] * 26
        for tile in tiles: record[ord(tile)-ord('A')] += 1
        def solution_737_1_2(record):
            s = 0
            for i in range(26):
                if not record[i]: continue
                record[i] -= 1
                s += solution_737_1_2(record) + 1 
                record[i] += 1
            return s    
        return solution_737_1_2(record)