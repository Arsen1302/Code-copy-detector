class Solution:
    def solution_676_3_1(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        def solution_676_3_2(prev,rem):
            if not rem:
                return 1

            ans = 0

            for i,a in enumerate(rem):
                if (i > 0 and a == rem[i-1]) or (prev != -1 and math.sqrt(prev+a)%1 != 0):
                    continue
                
                ans += solution_676_3_2(a,rem[:i]+rem[i+1:])
                
            
            return ans
        
        return solution_676_3_2(-1,nums)