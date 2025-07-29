class Solution:
    def solution_1696_5_1(self, num: int) -> bool:
        if num == 0:
            return True
        
        def solution_1696_5_2(n):
            rev = 0
            while n!=0:
                rev = rev*10+n%10
                n = n//10
            return rev
        
        for i in range(1, num+1):
            if i+solution_1696_5_2(i) == num:
                return True
                
        return False