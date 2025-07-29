class Solution:
    def solution_398_3_1(self, forest: List[List[int]]) -> int:
        Valid_target=sorted([(val,r,c)for r,row in enumerate(forest) for c,val in enumerate(row) if val>1],key=lambda x:x[0])
        sc=sr=ans=0
        
        for x in Valid_target:
            _,tr,tc=x
            d=self.solution_398_3_2(forest,sr,sc,tr,tc)
            if d<0:return -1
            ans+=d
            sr,sc=tr,tc
        return ans
            
    def solution_398_3_2(self,forest,sr,sc,tr,tc):
        R,C=len(forest),len(forest[0])
        Queue=collections.deque([(sr,sc,0)])
        seen={(sr,sc)}
        
        while Queue:
            r,c,d=Queue.popleft()
            
            if tr==r and tc==c: return d
            
            for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in seen and forest[nr][nc]:
                    seen.add((nr,nc))
                    Queue.append((nr,nc,d+1))
        return -1