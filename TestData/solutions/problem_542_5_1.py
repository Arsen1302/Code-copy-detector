class Solution:
    def solution_542_5_1(self, s1: str, s2: str) -> int:
        @cache
        def solution_542_5_2(a,b,pos):
            if a==b :
                return 0
            while a[pos]==b[pos] :
                pos+=1
            a,b=list(a),list(b)
            ans=10**18
            for i in range(pos+1,len(a)):
                if b[i]==a[pos] and b[i]!=a[i] :
                    b[i],b[pos]=b[pos],b[i]
                    ans=min(ans,solution_542_5_2(tuple(a),tuple(b),pos+1)+1)
                    b[i],b[pos]=b[pos],b[i]
            return ans
        return solution_542_5_2(tuple(s1),tuple(s2),0)