class Solution:
    def solution_1466_3_1(self, startWords: List[str], targetWords: List[str]) -> int:
        # represent chars in word with binary encoding "ca" = (1,0,1,...,0)
        def solution_1466_3_2(word):
            ans = [0]*26
            for c in word:
                ans[ord(c) - ord('a')] = 1
            return tuple(ans)
        
        # create set with binary encoded words
        words = set()
        for word in startWords:
            words.add(solution_1466_3_2(word))
        
        # for each targetWord remove one char and look in the set whether 
        # the reduced binary encoded character string is there
        ans = 0
        for word in targetWords:
            for i in range(len(word)):
                cutWord = word[:i] + word[i+1:]
                if solution_1466_3_2(cutWord) in words:
                    ans += 1
                    break
                
        return ans