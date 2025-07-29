class Solution:
    def solution_1488_5(self, num: int) -> int:
        isnegative = True if num<0 else False
        nums = str(num)
        if isnegative:
            nums = [(ch) for ch in nums[1:]]
            nums.sort(reverse = True)
            return -int(''.join(nums))
        if not isnegative:
            nums  = [ch for ch in nums]
            nums.sort()
            ## now find the range of 0roes 
            if nums[0] == '0':
                i = 0
                ans = '0'
                while i<len(nums) and nums[i]=='0':
                    i+=1
                if len(nums)>1:
                    ans = ''.join(nums[i:i+1]+nums[0:i]+nums[i+1:])
                return ans
       
            else:
                return int(''.join(nums))