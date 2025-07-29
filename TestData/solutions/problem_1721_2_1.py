class Solution:
    def solution_1721_2_1(self, s: str, k: int) -> int:
        n=len(s)
        def solution_1721_2_2(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        @lru_cache(2000)
        def solution_1721_2_3(i,j):
            if i>=n or j>=n or (j-i)>k+1:
                return 0
            if s[i]==s[j]:
                if solution_1721_2_2(i,j):
                    return 1+solution_1721_2_3(j+1,j+k)
            return max(solution_1721_2_3(i,j+1),solution_1721_2_3(i+1,j+1))
        return solution_1721_2_3(0,k-1)