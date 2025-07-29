class Solution:
    def solution_527_4_1(self, strs: List[str]) -> int:
        
        l=len(strs)
        self.rank=[1 for i in range(l)]
        group=[i for i in range(l)]
        
        p=len(strs[0])
        def solution_527_4_2(i,j):
            ct=0
            for a,b in zip(i,j):
                ct+=(a!=b)
                if ct>2:
                    return False
            return True
        
        def solution_527_4_3(i):
            if group[i]==i:
                return i
            return solution_527_4_3(group[i])

        def solution_527_4_4(i,j):
            a=solution_527_4_3(i)
            b=solution_527_4_3(j)
            if a!=b:
                if self.rank[a]>=self.rank[b]:
                    group[b]=a
                    self.rank[a]+=self.rank[b]
                    self.rank[b]=0
                else:
                    group[a]=b
                    self.rank[b]+=self.rank[a]
                    self.rank[a]=0

        for i in range(l):
            for j in range(i+1,l):
                y=solution_527_4_2(strs[i],strs[j])
                if y:
                    solution_527_4_4(i,j)
        count=0
        for i in self.rank:
            if i>0:
                count+=1
        return count