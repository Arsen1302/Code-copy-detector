class Solution:
    def solution_1513_1(self, nums: List[int]) -> List[int]:       

        stack = nums[:1]
        
        for j in range(1, len(nums)):
            cur = nums[j]
            while stack and math.gcd(stack[-1], cur) > 1:
                prev = stack.pop()
                cur = math.lcm(prev, cur)
            stack.append(cur)            
               
        return stack