class Solution:
    def solution_769_4_1(self, nums: List[int]) -> int:
        # try to make alternate less than left and right..
        def solution_769_4_2(start, nums): # returns cost
            cost = 0
            for i in range(start, len(nums), 2):
                
                # 1. make me smaller than LEFT adjacent
                if i > 0 and nums[i-1] <= nums[i]:
                    change = nums[i] - nums[i-1] + 1 # +1 as strict < not <=
                    cost += change
                    nums[i] -= change
                
                # 2. do same for right neighbour
                if i < len(nums)-1 and nums[i+1] <= nums[i]:
                    change = nums[i] - nums[i+1] + 1
                    cost += change
                    nums[i] -= change
            
            return cost
        
        return min(solution_769_4_2(0, nums[:]), solution_769_4_2(1,nums[:]))

    # cleaner and extensible to just take change to min(neighbours)
    def solution_769_4_3(self, nums: List[int]) -> int:
        # try to make alternate less than left and right..
        
        def solution_769_4_2(start): # returns cost
            cost = 0
            for i in range(start, len(nums), 2):
                change = 0
                # 1. make me smaller than LEFT adjacent
                if i > 0 and nums[i-1] <= nums[i]:
                    left_change = nums[i] - nums[i-1] + 1
                    change = max(left_change, change)
                
                # 2. do same for right neighbour
                if i < len(nums)-1 and nums[i+1] <= nums[i]:
                    right_change = nums[i] - nums[i+1] + 1
                    change = max(right_change, change)
                
                cost += change
            return cost
        
        return min(solution_769_4_2(0), solution_769_4_2(1))


"""
tests 
[1,2,3]
[9,6,1,6,2]
[1]
[1,2]
[2,1,2] 
"""