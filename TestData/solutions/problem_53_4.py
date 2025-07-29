class Solution:
    def solution_53_4(self, s: str, wordDict: List[str]) -> List[str]:        
        
        N = len(s)    
        queue, sentences = deque([(0, '')]), []
        while queue:
            i, sentence = queue.pop()
            if i == N: 
                sentences.append(sentence[1:])
                continue
            for word in wordDict:
                index = i+len(word)
                if index <= N and s[i:index] == word: 
                    queue.append((index, sentence+' '+word))
        return sentences