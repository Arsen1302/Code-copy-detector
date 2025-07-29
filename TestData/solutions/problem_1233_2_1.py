class Solution:
    def solution_1233_2_1(self, nums: List[int]) -> int:
        
        def solution_1233_2_2(num):
            return int(str(num)[::-1])
        
        for i in range(len(nums)):
            nums[i] = nums[i] - solution_1233_2_2(nums[i])
            
        count = 0
        freq = {}
        
        for i in nums:
            if i in freq.keys(): freq[i] += 1
            else: freq[i] = 1

        for k, v in freq.items():
            count += ((v * (v -1 )) // 2)
            
        return count % (10 ** 9 + 7)