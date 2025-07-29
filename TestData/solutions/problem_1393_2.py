class Solution:
    def solution_1393_2(self, s: str) -> bool:
        a=[]
        p="C"
        for i in s:
            if i==p:
                a[-1]+=1
            else:
                p=i
                a.append(1)
        odd,even=0,0
        for i in range(len(a)):
            if i%2:
                odd += max(0,a[i]-2)
            else:
                even += max (0,a[i]-2)
        if s[0]=="A" and even>odd:
            return True
        if s[0]=="B" and odd>even:
            return True
        return False