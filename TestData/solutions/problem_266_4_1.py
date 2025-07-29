class Solution:
    def solution_266_4_1(self, words: List[str]) -> List[str]:
        seen = set(words)
        
        @cache
        def solution_266_4_2(word):
            """Return True if input is a concatenated word."""
            for i in range(1, len(word)): 
                prefix = word[:i]
                suffix = word[i:]
                if prefix in seen and (suffix in seen or solution_266_4_2(suffix)): return True 
            return False 
        
        ans = []
        for word in words: 
            if solution_266_4_2(word): ans.append(word)
        return ans