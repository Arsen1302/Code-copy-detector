class Solution:
    def solution_612_3(self, A: List[int], S: int) -> int:
        ans = ii = rsm = val = 0
        for i in range(len(A)): 
            if A[i]:
                rsm += A[i] # range sum 
                val = 0
                while ii < len(A) and rsm == S: 
                    rsm -= A[ii]
                    ii += 1
                    val += 1
            else: val += int(S == 0) # edge case 
            ans += val
        return ans