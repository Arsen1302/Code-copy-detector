class Solution:
    def solution_1725_4_1(self, s: str, k: int, min_len: int) -> int:
        n=len(s)
        mod=10**9+7
        prime=set(['2','3','5','7'])
        if s[0] not in prime or s[-1] in prime: return 0
        arr=[]
        last,i=0,1
        while i<n:
            if (i==n-1) or (s[i] not in prime and s[i+1] in prime):
                arr.append(i-last+1)
                last=i+1
                i+=2
            else:
                i+=1
        pre_sum={-1:0}
        m=len(arr)
        next_idx=[-1]*m
        for i,val in enumerate(arr):
            pre_sum[i]=pre_sum[i-1]+val
        for i in range(m):
            for j in range(i+1,m+1):
                if pre_sum[j-1]-pre_sum[i-1]>=min_len:
                    next_idx[i]=j-1
                    break
        @cache
        def solution_1725_4_2(idx,length,started):
            if idx==m:
                return 1 if (length==k and not started) else 0
            ans=0
            if started:
                #end here
                ans+=solution_1725_4_2(idx+1,length+1,0)
                #don't end here
                ans+=solution_1725_4_2(idx+1,length,1)
            else:
                #start from here
                if next_idx[idx]!=-1: 
                    ans+=solution_1725_4_2(next_idx[idx],length,1)
            return ans%mod
        return solution_1725_4_2(0,0,0)