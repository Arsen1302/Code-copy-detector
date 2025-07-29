class Solution:
    #Let n = len(nums)!
    #Time-Complexity: O(log(max(nums)) * n)
    #Space-Complexity: O(1)
    def solution_839_4_1(self, nums: List[int], threshold: int) -> int:
        #Approach: Define the search space for divisors, ranging from 1 to 
        #maximum element in input array nums!
        
        #Perform binary search on such search space and update minimal divisor
        #s.t. it meets the condition as we go!
        
        #Once binary search stops, the answer variable should store value
        #which is the minimal divisor to not exceed threshold!
        
        #define a solution_839_4_2 function to find sum of elements after dividing each
        #and every element in nums by divisor!
        
        def solution_839_4_2(divisor):
            nonlocal nums
            accumulator = 0
            for e in nums:
                divided = e / divisor
                #if it's integer, leave it!
                if(divided.is_integer()):
                    accumulator += int(divided)
                    continue
                else:
                    divided = int(divided)
                    #round up
                    divided += 1
                    accumulator += divided
            return accumulator
        
        
        L, H = 1, max(nums)
        ans = None
        while L <= H:
            cur = (L + H) // 2
            total_sum = solution_839_4_2(cur)
            #check against the threshold!
            if(total_sum <= threshold):
                ans = cur
                H = cur - 1
                continue
            else:
                L = cur + 1
                continue
        return ans