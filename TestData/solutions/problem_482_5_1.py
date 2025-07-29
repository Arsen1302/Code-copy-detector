class Solution:
    def solution_482_5_1(self,original,new,index):
        for ch in new:
            index= original.find(ch,index)
            if index==-1:return False
            index+=1
        return True
    def solution_482_5_2(self, s: str, words: List[str]) -> int:
        ans=0
        for w in words:ans+=self.solution_482_5_1(s,w,0)
        return ans