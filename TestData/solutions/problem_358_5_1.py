class Solution(object):
    '''
       As we know inorder to check if a triangle is valid or not, if its sides are given:=>
       A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is 
       greater than the third side. For Example, let A, B and C are three sides of a triangle. 
       Then, A + B > C, B + C > A and C + A > B.
       Following the same we can apply this in code... 
    '''
    def solution_358_5_1(self,index,nums):
        l,r = 0, index-1
        ans  = 0
        while l < r:
            if nums[l] + nums[r] > nums[index]:
                ans += r - l
                r -= 1
            else:
                l += 1    
        return ans
    
    def solution_358_5_2(self, nums):
        if len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            res += self.solution_358_5_1(i, nums) 
        
        return res