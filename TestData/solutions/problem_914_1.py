class Solution:
    def solution_914_1(self, light: List[int]) -> int:
        max = count = 0
        for i in range(len(light)):
            if max < light[i]:
                max = light[i]
            if max == i + 1:
                count += 1
        return count