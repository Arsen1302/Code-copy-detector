class Solution:
    def solution_1561_3(self, num: str) -> str:
        num = "0"+num+"0"
        i=0
        l=len(num)
        max_=-1
        for i in range(1,l-1):
            if num[i]==num[i-1]==num[i+1]:
                max_=max(int(num[i]),max_)
        if max_==-1:
            return ""
        return str(max_)*3