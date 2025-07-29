class Solution:
    def solution_1368_3_1(self, s: str) -> int:
        self.answer = 0
        
        def solution_1368_3_2(i, word, word2):
            if i >= len(s):
                if word == word[::-1] and word2 == word2[::-1]:
                    self.answer = max(len(word) * len(word2), self.answer)
                return
            
            solution_1368_3_2(i + 1, word + s[i], word2)
            solution_1368_3_2(i + 1, word, word2 + s[i])
            solution_1368_3_2(i + 1, word, word2)
            
        solution_1368_3_2(0, '', '')
        
        return self.answer