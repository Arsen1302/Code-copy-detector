class Solution:
    def solution_324_5_1(self, isConnected: List[List[int]]) -> int:
#  set all parents value to 1 that is node is a parent of itself
        par=[i for i in range(len(isConnected))]
#  rank is the length of the particular component at that index, initially all are disjoint components so default to 1
        rank=[1]*(len(isConnected))

        def solution_324_5_2(n):
            p=n
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def solution_324_5_3(n1,n2):
            p1,p2=solution_324_5_2(n1),solution_324_5_2(n2)
            if p1==p2:
                return 0
#  if parent of p1 is greater than the parent of p2 , then set p2's parent as p1 and increment the rank of p1
            if par[p1]>par[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
#  if parent of p2 is greater than the parent of p1 , then set p1's parent as p2 and increment the rank of p2
                par[p1]=p2
                rank[p2]+=rank[p1]
            return 1
# keep track of the total count (i.e initially we consider all components are disjoint so count is nothing but a length of the array itself )
        count=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
# traverse through array and if we solution_324_5_2 the connection between node i and j that is represented as 1 in the question, then it means that our connected component is decreasing by return value of solution_324_5_3 function so count-=solution_324_5_3(i,j)
                if isConnected[i][j]==1:
                    count-=solution_324_5_3(i,j)
        return count