class Solution:
    def solution_82_1(self, s: str) -> List[str]:
        
        res, d = [], {}
        for i in range(len(s)):
            
            if s[i:i+10] not in d: d[s[i:i+10]] = 0
            elif s[i:i+10] not in res: res.append(s[i:i+10])
                
        return res
		
		# An Upvote will be encouraging