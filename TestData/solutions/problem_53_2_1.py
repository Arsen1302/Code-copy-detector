class Solution:
    def solution_53_2_1(self, s, wordDict, start, cur, res):
        # Base Case
        if start == len(s) and cur:
            res.append(' '.join(cur))
            
        for i in range(start, len(s)):
            word = s[start: i+1]
            
            if word in wordDict:
                
                # Append the word since it is in the dictionary
                cur.append(word)
                
                # Recursive Step
                self.solution_53_2_1(s, wordDict, i+1, cur, res)
                
                # Backtracking / Post-processing / Pop the word we appended
                cur.pop()
        
    def solution_53_2_2(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.solution_53_2_1(s, set(wordDict), 0, [], res)
        return res