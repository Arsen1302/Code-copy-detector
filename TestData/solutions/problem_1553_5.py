class Solution:
    def solution_1553_5(self, words: List[str], s: str) -> int:
        st = 0
        count = 0
        for pre in words:
            n = len(pre)
            st = 0
            if n==1:
                if s[0] == pre:
                    count+=1
            else: 
                if n<=len(s):
                    while (st<n):
                        print(pre[st],s[st])
                        print(count)
                        if pre[st]!=s[st]:
                            break
                        if st==n-1:
                            count+=1
                        st=st+1
                
        return count