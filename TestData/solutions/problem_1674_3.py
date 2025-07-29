class Solution:
    def solution_1674_3(self, words: List[str]) -> List[int]:
        
        prefs = {}
        
        ans = []
        
        for w in words:
            for i in range(1, len(w)+1):
                if w[0:i] not in prefs:
                    prefs[w[0:i]] = 1
                else:
                    prefs[w[0:i]] += 1
                    
        for i, w in enumerate(words):
            for j in range(1, len(w)+1):
                if i >= len(ans):
                    ans.append(prefs[w[0:j]])
                else:
                    ans[i] += prefs[w[0:j]]
        

        return ans