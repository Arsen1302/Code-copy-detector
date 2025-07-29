class Solution:
    def solution_183_4(self, num: int) -> bool:
        left,right = 1,num
        while left<=right:
            middle = (left+right)//2
            if middle**2==num:
                return True
            if middle**2>num:
                right = middle-1
            else:
                left = middle+1
        return False