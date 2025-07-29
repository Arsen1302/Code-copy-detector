class Solution:
    def solution_1294_2_1(self, s: str, p: str, removable: List[int]) -> int:
        
        def solution_1294_2_2(s,subseq,removed):
            i = 0
            j  = 0
            while i<len(s) and j<len(subseq):
                if i in removed or s[i]!= subseq[j]:
                    i+=1
                    continue
                i+=1
                j+=1
            return j == len(subseq)
        
        removed = set()
        l = 0
        r = len(removable)-1
        ans = 0
        while l<=r:
            mid  = l+(r-l)//2
            removed = set(removable[:mid+1])
            if solution_1294_2_2(s,p,removed):
                ans = max(ans,len(removed))
                l = mid+1
                
            else:
                r = mid-1
        return ans