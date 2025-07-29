class Solution:
    def solution_773_5(self, n: int, k: int, target: int) -> int:
        # set up the variables 
        t = target - n
        ret = 0
        l = 0
        m = 10**9 + 7
        # polynomial multiplication
        while l*k <= t:
            r = t - l*k # find the correct power of the second term
            #              first coefficient   |  second coefficient
            ret = (ret + ((-1)**l) * comb(n,l) * comb(r+n-1,n-1)) % m
            l += 1
        return ret