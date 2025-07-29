class Solution:
    def solution_516_4(self, s):
        indices=defaultdict(list)
        for i in range(len(s)):
            indices[s[i]].append(i)
        
        r=0
        for k,v in indices.items():
            for i in range(len(v)):
                curr=v[i]
                if i==0:
                    prev=-1
                else:
                    prev=v[i-1]
                
                if i==len(v)-1:
                    nxt=len(s)
                else:
                    nxt=v[i+1]
                    
                r+=(curr-prev)*(nxt-curr)
        return r