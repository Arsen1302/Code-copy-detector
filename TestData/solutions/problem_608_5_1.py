class Solution:
    def solution_608_5_1(self, s: str) -> int:
        def solution_608_5_2(nums):
            res = []
            cur_sum = 0
            for num in nums:
                cur_sum += num
                res.append(cur_sum)
            return res
        def solution_608_5_3(nums):
            res = []
            cur_sum = 0
            for num in reversed(nums):
                cur_sum += 1 - num
                res.append(cur_sum)
            return list(reversed(res))
        
        nums = [int(i) for i in s]
        print(nums) # [0, 0, 1, 1, 0]
        prefix_sum = [0] + solution_608_5_2(nums)
        print(prefix_sum) # [0, 0, 0, 1, 2, 2]
        suffix_sum = solution_608_5_3(nums) + [0]
        print(suffix_sum) # [3, 2, 1, 1, 1, 0]
             
        #              [0, 0, 0, 1, 2, 2]
        #               +  +  +  +  +  +
        #              [3, 2, 1, 1, 1, 0]
        #        
        #   return min([3, 2, 1, 2, 3, 2])
        
        return min([pre + suf for pre, suf in zip(prefix_sum, suffix_sum)])