class Solution:
    def solution_790_4(self, s: str) -> str:
        stk,arr=[],[]
        for i in s:
            if i!=')':
                stk.append(i)
            else:
                popele=stk.pop()
                while popele!='(':
                    arr.append(popele)
                    popele=stk.pop()

                for j in arr:
                    stk.append(j)
                arr=[]
        ans=''
        for k in stk:
            ans+=k
        return ans
	```