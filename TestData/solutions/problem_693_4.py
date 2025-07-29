class Solution:
    def solution_693_4(self, arr: List[int]) -> bool:
        s=sum(arr)/3
        if(s!=int(s) or len(arr)<3):
            return False
        x=0
        c=0
        for i in range(len(arr)-1):
            x+=arr[i]
            if(c==2):
                break
            if(x==s):
                x=0
                c+=1
        return c==2