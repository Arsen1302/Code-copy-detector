```class Solution:
    def solution_1312_1(self, n: int) -> int:
        count = 0
        sqrt = 0
        for i in range(1,n-1):
            for j in range(i+1, n):
                sqrt = ((i*i) + (j*j)) ** 0.5
                if sqrt % 1 == 0 and sqrt <= n:
                    count += 2
        return (count)
		

*Please Upvote if you like*