class Solution:
    def solution_266_2_1(self, words: List[str]) -> List[str]:
        s = set(words)
        
        memo = {}
        def solution_266_2_2(w):
            if w in memo: return memo[w]
            
            for i in range(1, len(w)):
                if w[:i] not in s: continue
                
                r = w[i:]
                if r in s or solution_266_2_2(r):
                    memo[w] = True
                    return True
                
            memo[w] = False
            return False
        
        return filter(solution_266_2_2, words)