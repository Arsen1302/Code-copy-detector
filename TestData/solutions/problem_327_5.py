class Solution(object):
    def solution_327_5(self, nums):

        A = list(map(str, nums))
        
        
        if len(A) <= 2:
            
            return '/'.join(A)
        
        
        return A[0] + '/(' + '/'.join(A[1:]) + ')'