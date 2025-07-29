class Solution:
    def solution_1107_4_1(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        n,m = len(target),len(words[0])
        
        frequency = defaultdict(int)
        for word in words:
            for i,ch in enumerate(word):
                frequency[(ch,i)]+=1

        dp = {}
        def solution_1107_4_2(i,j):
            if j == n: return 1
            if i == m: return 0
            if n-j > m-i: return 0

            if (i,j) in dp: return dp[(i,j)]

            take,not_take = 0,0
            not_take = solution_1107_4_2(i+1,j)%MOD
            if frequency[(target[j],i)] > 0:
                take = solution_1107_4_2(i+1,j+1)*frequency[(target[j],i)]%MOD
            
            dp[(i,j)] = (take+not_take)%MOD
            return dp[(i,j)]

        return solution_1107_4_2(0,0)%MOD