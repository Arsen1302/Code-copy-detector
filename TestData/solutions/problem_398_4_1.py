class Solution:
    def solution_398_4_1(self, forest: List[List[int]]) -> int:
        Valid_target=sorted([(val,r,c)for r,row in enumerate(forest) for c,val in enumerate(row) if val>1],key=lambda x:x[0])
        sc=sr=ans=0
        
        for x in Valid_target:
            _,tr,tc=x
            d=self.solution_398_4_2(forest,sr,sc,tr,tc)
            if d<0:return -1
            ans+=d
            sr,sc=tr,tc
        return ans
            
    def solution_398_4_2(self,forest,sr,sc,tr,tc):
        R,C=len(forest),len(forest[0])
        heap=[(0,0,sr,sc)]
        cost={(sr,sc):0}
        
        while heap:
            f,g,r,c=heapq.heappop(heap)
            
            if tr==r and tc==c: return g
            
            for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<R and 0<=nc<C and forest[nr][nc]:
                    New_cost=g+1+abs(nr-tr)+abs(nc-tr)
                    if New_cost<cost.get((nr,nc),99999):
                        cost[(nr,nc)]=New_cost
                        heapq.heappush(heap,(New_cost,g+1,nr,nc))
        return -1