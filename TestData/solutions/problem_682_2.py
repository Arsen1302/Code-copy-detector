class Solution:
    def solution_682_2(self, A: List[str]) -> List[str]:
        ans = []
        for i in set(A[0]):
            x = []
            for j in A:
                x.append(j.count(i))
            a = 0
            while a < min(x):
                ans.append(i)
                a += 1
        return ans