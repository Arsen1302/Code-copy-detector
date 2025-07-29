class Solution:
    def solution_501_5_1(self, A: List[int], K: int) -> float:
        s=[0]
        for i in A:
            s.append(i+s[-1]);
        n=len(s);
        mini= -200000
        d={};
        def solution_501_5_2(old,new,k):
            temp=(old,new,k);
            if(temp in d.keys()): return d[temp]
            if(new>=n) or (old>=n):
                return mini;
            if(k==1):
                return (s[-1]-s[old])/(n-1-old);
            d[temp]= max(solution_501_5_2(old,new+1,k),solution_501_5_2(new,new+1,k-1)+((s[new]-s[old])/(new-old)) );
            return d[temp]
        return solution_501_5_2(0,1,K);
		```