class Solution:
    def solution_1537_3(self, expression: str) -> str:
        [num1, num2] = expression.split('+')
        min_exp, min_val = '', float('inf')
        for i in range(len(num1)):
            for j in range(1,len(num2)+1):
                new_exp = num1[:i] + '(' + num1[i:] + '+' + num2[:j] + ')' + num2[j:] 
                new_val = 1
                if len(num1[:i])>0:
                    new_val = int(num1[:i])
                new_val = new_val * (int(num1[i:]) + int(num2[:j]))
                if len(num2[j:])>0:
                    new_val = new_val * int(num2[j:])
                if new_val < min_val:
                    min_val = new_val
                    min_exp = new_exp
        return min_exp