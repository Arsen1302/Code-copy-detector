class Solution:
    def solution_244_3(self, chars: List[str]) -> int:
        res=l=r=0
        while l<len(chars):
            while r<len(chars) and chars[l]==chars[r]:
                r+=1
            temp=chars[l]+str(r-l) if r-l>1 else chars[l]
            for c in temp:
                chars[res]=c
                res+=1
            l=r
        return res