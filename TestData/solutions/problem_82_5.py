class Solution:
    def solution_82_5(self, s: str) -> List[str]:
        ans, seen = set(), set()
        for i in range(len(s)-9): 
            ss = s[i:i+10]
            if ss in seen: ans.add(ss)
            seen.add(ss)
        return ans