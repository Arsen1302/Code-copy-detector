class Solution:
    def solution_124_5(self, nums: List[int], k: int) -> List[int]:
        rlist = []
        for i in range(len(nums)):
            if (i+k) > len(nums):
                break
            int_list = nums[i:(i+k)]
            max_element = max(int_list)
            rlist.append(max_element)
        return rlist