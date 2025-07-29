class Solution:
    def solution_585_2(self, s: str, k: int) -> str:
        st=""
        lst=list(s)
        lst.sort()
        queue=list(s)
        flg=defaultdict(lambda :0)
        if k==1:
            pt=[z for z in range(len(lst)) if s[z]==lst[0]]
            mn=s[pt[0]:]+s[:pt[0]]
            for p in range(len(pt)):
                mn=min(mn,s[pt[p]:]+s[:pt[p]])
            return mn
        ct=k
        if k==len(s):
            return "".join(lst)
        while k>0:
            if queue[0][0]==lst[0]:
                st+=queue.pop(0)[0]
                lst.pop(0)
                k-=1
                for nm in flg:
                    flg[nm]=0
            else:
                mn=queue[0]
                ind=0
                for i in range(1,min(ct,len(queue)-1)):
                    if queue[i]<mn and queue[i]!=lst[0] and flg[queue[i]]!=1:
                        ind=i
                x=queue.pop(ind)
                queue.append(x)
                flg[x]=1
        if ct>1:
            queue.sort()
        return st+"".join(queue)