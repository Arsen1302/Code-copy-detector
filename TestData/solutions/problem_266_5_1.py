class Solution:
    def solution_266_5_1(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        res = []
        # for each word, remove it from the set and call solution_266_5_2 and add it back for next iteration
        for word in words:
            wordSet.remove(word)
            if self.solution_266_5_2(wordSet, word, {}):
                res.append(word)
            wordSet.add(word)
        return res
    
    def solution_266_5_2(self, wordSet: List[str], word: str, m: dict) -> bool:
        # base case: return True if a string can be found,
        # originally I was thinking of base case being len(word) == 0, but it is not true because my subproblem is if the substring in word can be concatenated using wordSet. So base case should be what is the smallest substring that is in the wordSet
        if word in wordSet:
            return True
        
        # memoization would be a dict of all the substring and whether is true of not
        if word in m:
            return m[word]
        
        # go from the end of string to index 1(1 so that smallest string is the first index)
        for i in range(len(word) - 1, 0, -1):
            if word[i:] in wordSet and self.solution_266_5_2(wordSet, word[:i], m):
                m[word] = True
                return True
        m[word] = False
        return False