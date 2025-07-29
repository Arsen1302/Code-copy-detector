class Solution:
    def solution_612_2(self, A: List[int], S: int) -> int:
        ans = ii = rsm = val = 0
        for i, x in enumerate(A): 
            rsm += x
            if x: val = 0
            while ii <= i and rsm >= S: 
                if rsm == S: val += 1
                rsm -= A[ii]
                ii += 1
            ans += val
        return ans