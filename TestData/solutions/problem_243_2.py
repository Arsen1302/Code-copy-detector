class Solution:
    def solution_243_2(self, N: List[int]) -> List[int]:
        A = []
        for n in N:
            if N[abs(n)-1] > 0: N[abs(n)-1] = -N[abs(n)-1]
            else: A.append(abs(n))
        return A



- Junaid Mansuri
(LeetCode ID)@hotmail.com