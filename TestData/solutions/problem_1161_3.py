class Solution:
    def solution_1161_3(self, n: int) -> int:
		#here s is sum of 1 to 7	
        s = 28
        res = 0
        if n>7:
            res = s
            div = n//7
            for i in range(1,div):
                res+=s+7*i
            rem = n%7
            for i in range(1,rem+1):
                res+=i+div
        else:
            for i in range(1,n+1):
                res+=i
        return res