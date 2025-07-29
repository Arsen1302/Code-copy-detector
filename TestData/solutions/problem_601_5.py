class Solution:
    def solution_601_5(self, nu: List[int]) -> int:
        ma = float("-inf")
        mi = float("inf")
        t1 = 0
        t2 = 0
        an = 0
        nm = float("-inf")
        for i in range(len(nu)):
            if nu[i]>nm:
                nm = nu[i]
            an += nu[i]
            if nu[i] >= 0:
                t1 += nu[i]
            else:
                if t1+nu[i]>=0:
                    t1 += nu[i]
                else:
                    t1 = 0
            if nu[i] <= 0:
                t2 += nu[i]
            else:
                if t2 + nu[i]<0:
                    t2 += nu[i]
                else:
                    t2 = 0
            ma = max(ma,t1)
            mi = min(mi,t2)
        if nm<=0:
            return nm
        return max(ma,an-mi)