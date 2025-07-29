class Solution:
    def solution_328_2(self, wall: List[List[int]]) -> int:
        table = dict()
        for row in wall:
            tmp_sum = 0
            for item in row:
                tmp_sum += item
                if tmp_sum not in table:
                    table[tmp_sum] = 1
                else:
                    table[tmp_sum] += 1
        output = len(wall)
        for key in table:
            if len(wall) - table[key] < output and key != sum(wall[0]):
                output = len(wall) - table[key]
        return output