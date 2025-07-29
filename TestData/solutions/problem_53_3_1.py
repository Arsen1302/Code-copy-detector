class Solution:
    class Trie:
        def solution_53_3_1(self):
            self.root = {}
            self.WORD_DELIM = '$'
            
        def solution_53_3_2(self, word):
            cur = self.root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.WORD_DELIM] = word
            
        def solution_53_3_3(self, words):
            for word in words:
                self.solution_53_3_2(word)
                
        def solution_53_3_4(self, word, res = ''):            
            res = []
            def solution_53_3_5(word=word, temp=[]):
                cur = self.root
                for i,char in enumerate(word):
                    if self.WORD_DELIM in cur:
                        solution_53_3_5(word[i:], temp + [cur[self.WORD_DELIM]])
                    if char not in cur:
                        break
                    cur = cur[char]
                else:
                    if self.WORD_DELIM in cur:
                        res.append(' '.join(temp + [cur[self.WORD_DELIM]]))
            solution_53_3_5()
            return res
                
    def solution_53_3_6(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.Trie()
        trie.solution_53_3_3(wordDict)
        return trie.solution_53_3_4(s)