class Solution:
    def solution_914_2(self, light: List[int]) -> int:
        res = 0
        curr_sum = 0
        object_sum = 0
        for i, bulb in enumerate(light):
            object_sum += i + 1
            curr_sum += bulb
            if curr_sum == object_sum:
                res += 1
        return res