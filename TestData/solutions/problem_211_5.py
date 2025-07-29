class Solution:
    def solution_211_5(self, n: int) -> int:
        if len(str(n))==1:
            return n
        c=1
        while n>=9*(10**(c-1))*c:
            n-=9*(10**(c-1))*c
            c+=1
        if n==0:
            return 9
        a=10**(c-1)-1
        a+=n//c
        if n%c!=0:
            a+=1
        if n%c==0:
            return int(str(a)[-1])
        else:
            return int(str(a)[(n%c)-1])