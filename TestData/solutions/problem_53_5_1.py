class Solution:
    def solution_53_5_1(self, s: str, wordDict: List[str]) -> List[str]:
    
        def solution_53_5_2(i = 0, sentence = ''):
            nonlocal N
            if i == N: 
                sentences.append(sentence[1:])
                return
            for word in wordDict:
                index = i+len(word)
                if index <= N and s[i:index] == word and i not in visited:
                    visited.add(i)
                    solution_53_5_2(index, sentence+' '+word)
                    visited.remove(i)
            
        N = len(s)
        sentences, visited = [], set()
        solution_53_5_2()
        return sentences