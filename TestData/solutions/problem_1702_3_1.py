class Solution:
    def solution_1702_3_1(self, words: List[str]) -> str:
        def solution_1702_3_2(word):
            return [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]
        
        diff1 = solution_1702_3_2(words[0])
        diff2 = solution_1702_3_2(words[1])
        for word in words[2:]:
            curDiff = solution_1702_3_2(word)
            if curDiff != diff1 and curDiff != diff2:
                return word
            elif curDiff != diff1:
                return words[0]
            elif curDiff != diff2:
                return words[1]