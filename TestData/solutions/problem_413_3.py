class Solution:
    def solution_413_3(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        degree = max(dic.values())
        if degree == 1:
            return 1
        else:
            min_length = len(nums)
            for keys in dic:
                if dic[keys] == degree:
                    pos1 = nums.index(keys)
                    pos2 = len(nums) -nums[::-1].index(keys) - 1
                    if pos2 - pos1 + 1 < min_length:
                        min_length = pos2 - pos1 + 1
        return min_length