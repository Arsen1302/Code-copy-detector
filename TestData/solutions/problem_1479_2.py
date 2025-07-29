class Solution:
    def solution_1479_2(self, statements: List[List[int]]) -> int:
        ans, n = 0, len(statements)
        for mask in range(1 << n):                           # 2**n possibilities
            valid = True
            for i in range(n):
                if not (mask >> i) &amp; 1: continue             # check if the `i`th person is a `good` person
                for j in range(n):
                    if statements[i][j] == 2: continue
                    elif statements[i][j] != (mask >> j) &amp; 1:# check if `i`th person's statement about `j` matches what `mask` says
                        valid = False
                        break                                # optimization: break the loop when not valid
                if not valid: 
                    break                                    # optimization: break the loop when not valid
            if valid: 
                ans = max(ans, bin(mask).count('1'))         # count `1` in mask, take the largest
        return ans