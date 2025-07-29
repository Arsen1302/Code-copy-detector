class Solution:
    def solution_242_1(self, n: int) -> int:

        first = 1
        last = n
        if n==1:
            return 1
        while first <= last:
            mid = (first+last)//2

            if mid*(mid+1) == 2*n:
                return mid
            elif mid*(mid+1) > 2*n:
                last = mid-1
            else:
                first = mid+1
        return last