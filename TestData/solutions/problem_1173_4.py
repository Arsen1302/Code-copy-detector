class Solution:
    def solution_1173_4(self, gain: List[int]) -> int:
        new_arr = [0]
        a = 0
        for i in gain:
            a+=i
            new_arr.append(a)
        return max(new_arr)