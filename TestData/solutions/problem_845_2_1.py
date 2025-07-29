class Solution:
    def solution_845_2_1(self, low: int, high: int) -> List[int]:
        ans = []
        def solution_845_2_2(cur, digit):
            if digit <= 10 and low <= cur <= high: ans.append(cur) # add number satisfy the condition
            elif cur < low: pass                                   # continue check larger values
            else: return                                           # stop condition
            cur = cur * 10 + digit                                 # generating number with sequential digits
            solution_845_2_2(cur, digit+1)                                      # backtracking
        for i in range(1, 10): solution_845_2_2(0, i)                           # start with each digit from 1 to 9, inclusive
        return sorted(ans)                                         # sort the result and return