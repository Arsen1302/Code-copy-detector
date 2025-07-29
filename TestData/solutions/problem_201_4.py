class Solution:
    def solution_201_4(self, n: int) -> int:
        first=1
        distance=1
        step=0
        while n>1:
            if step%2==0 or n%2!=0:
                first+=distance
			# Multiply distance by 2
            distance=distance<<1
            step+=1
			# Divide n by 2
            n=n>>1
        return first