class Solution:
    def solution_1490_5(self, num1: int, num2: int) -> int:
        
        # this important here in case one of them equal 0 or both equal 0 
		# in this case we will not enter while loop
		cnt = 0
        while min(num1, num2) > 0:
            if num1 >= num2:
                cnt += num1 // num2
                num1 = num1 % num2
            else:
                cnt += num2 // num1
                num2 = num2 % num1
        
        return cnt