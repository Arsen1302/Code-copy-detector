class Solution:
    def solution_940_4(self, words: List[str]) -> List[str]:
        words.sort(key=len) #by size in ascending order 
        ans = []
        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                if word in words[j]: 
                    ans.append(word)
                    break
        return ans