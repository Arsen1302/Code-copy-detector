class Solution:
    def solution_941_4_1(self, queries: List[int], m: int) -> List[int]:
        p=[i for i in range(m+1)]
        scnt=1
        rcnt=0
        sh={}
        ans=[]
        def solution_941_4_2(v, l, r):
            mid=(r+l)//2
            mval=p[mid]
            while mval!=v:
                if v>mval:
                    l=mid+1
                else:
                    r=mid-1
                mid=(l+r)//2
                mval=p[mid]
            return mid
        for v in queries:
            if v not in sh: 
                l=max(scnt, v)
                r=min(l+v-p[l], m)
                pos=solution_941_4_2(v, l, r)
                sh[v]=[scnt, rcnt]
                scnt+=1
            else:
                l=scnt-sh[v][0]
                r=l+rcnt-sh[v][1]
                for i in range(l, r+1):
                    if p[i]==v:
                        pos=i
                        break
                sh[v]=[scnt, rcnt]
                rcnt+=1
            ans.append(pos-1)  #p is 1-indexed unlike the answer
            p.insert(1, p.pop(pos))
        return ans