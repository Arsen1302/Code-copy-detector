class Solution:
    def solution_1107_2_1(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        n,m = len(target),len(words[0])
        
        def solution_1107_2_2(i,j):
            if j == n: return 1
            if i == m: return 0
            if n-j > m-i: return 0

            res = 0
            for word in words:
                for k in range(i,m):
                    if word[k] == target[j]:
                        res += solution_1107_2_2(k+1,j+1)

            return res

        return solution_1107_2_2(0,0)%MOD