# Solution - I
class Solution:
    def solution_1190_5_1(self, a, b, c):
        if (a >= b) and (a >= c):
            solution_1190_5_2 = a
        elif (b >= a) and (b >= c):
            solution_1190_5_2 = b
        else:
            solution_1190_5_2 = c
        s = a+b+c
        if s-solution_1190_5_2<=solution_1190_5_2:
            return s - solution_1190_5_2
        return s//2
        ```
	
# Solution - II
class Solution:
    def solution_1190_5_1(self, num1, num2, num3):
        def solution_1190_5_2(num1, num2, num3):
            if (num1 > num2) and (num1 > num3):
                largest_num = num1
            elif (num2 > num1) and (num2 > num3):
                largest_num = num2
            else:
                largest_num = num3
            return largest_num 
        l = solution_1190_5_2(num1,num2,num3)
        s = num1+num2+num3
        if s-l<=l:
            return s-l
        return s//2