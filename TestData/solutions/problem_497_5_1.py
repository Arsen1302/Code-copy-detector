class Solution:
    def solution_497_5_1(self, s: str, words: List[str]) -> int:
        def solution_497_5_2(word):
            size = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    size += 1
                else:
                    yield word[i - 1], size
                    size = 1
            
            yield word[-1], size
            yield ' ', 0
        
        res = len(words)
        
        for word in words:
            for (sChar, sSize), (wordChar, wordSize) in zip(solution_497_5_2(s), solution_497_5_2(word)):
                if sChar != wordChar or sSize < wordSize or wordSize < sSize < 3:
                    res -= 1
                    break
        
        return res