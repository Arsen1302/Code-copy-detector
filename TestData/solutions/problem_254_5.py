class Solution:
    def solution_254_5(self, g: List[int], s: List[int]) -> int:
        ans=0 ; j=0 ; g.sort() ; s.sort()
        for i in range(len(g)):
            while j<len(s):
                if g[i]<=s[j]: ans+=1 ; s.remove(s[j]) ; break
                j+=1
        return ans