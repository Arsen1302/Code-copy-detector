class Solution:
    def solution_546_1(self, s: str, goal: str) -> bool:

        freq1=[0]*26
        freq2=[0]*26
        diff =0

        if(len(s)!=len(goal)):
            return False
        for i in range(len(s)):
            if(s[i]!=goal[i]):
                diff+=1
            freq1[ord(s[i])-ord('a')]+=1
            freq2[ord(goal[i])-ord('a')]+=1
        unique= True
        for idx in range(len(freq1)):
            if(freq1[idx]!=freq2[idx]):
                return False
            if(freq1[idx]>1):
                unique = False
        if(diff==2 or (unique==False and diff==0)):
            return True