class Solution(object):
    def solution_366_4(self, c):
        l,r = 0,int(sqrt(c))
        while l<=r:
            b = l+(r-1)//2
            if b*b == c:
                return True
            elif b*b < c:
                l=b+1
            else:
                r=b-1
        return False