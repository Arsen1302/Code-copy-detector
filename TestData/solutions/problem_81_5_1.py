class Solution:
    def solution_81_5_1(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def solution_81_5_2(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(solution_81_5_2))
        return str(int(str(''.join(nums))))