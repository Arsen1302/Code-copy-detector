class Solution:
    def solution_40_3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        if endWord not in wordList:
            return 0
        
        q = [(beginWord, 1)]
        wordList = set(wordList) # TLE if you don't convert into a set 
        seen = set([beginWord])
        
        while q:           
            currWord, level = q.pop(0)
            for i in range(len(currWord)):
                for j in range(97,123):
                    newWord = currWord[:i] + chr(j) + currWord[i+1:]
                    if newWord == endWord:
                        return level + 1
                    if newWord in wordList and newWord not in seen:
                        seen.add(newWord)
                        q.append((newWord, level+1))
                    
        return 0
                
            ```