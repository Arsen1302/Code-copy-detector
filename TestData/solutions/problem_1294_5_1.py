class Solution:
    # ////// TC: O(n * logk) //////
    # //// Checking is subsequence or not ////
    def solution_1294_5_1(self,s,subStr,removed):
        i,j = 0,0
        while i < len(s) and j < len(subStr):
            if s[i] != subStr[j] or i in removed:
                i += 1
                continue
            i += 1
            j += 1
        return j == len(subStr)
    
    
    def solution_1294_5_2(self, s: str, p: str, removable: List[int]) -> int:
        res = 0
        l,r = 0,len(removable) - 1
        while l <= r:
            mid = (l+r)//2
            removed = set(removable[:mid+1])
            if self.solution_1294_5_1(s,p,removed):
                res = max(res,mid+1)
                l = mid + 1  
            else:
                r = mid - 1
        return res