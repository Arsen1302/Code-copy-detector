class Solution:
    def solution_682_3(self, A: List[str]) -> List[str]:
        arr = []
        for i in set(A[0]):
            ans = [A[0].count(i)]
            for j in A[1:]:
                if(i in j):
                    ans.append(j.count(i))
            if(len(ans) == len(A)):
                arr += ([i] * min(ans))
        return arr