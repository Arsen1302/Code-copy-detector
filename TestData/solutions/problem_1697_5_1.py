```class Solution:
    def solution_1697_5_1(self, nums: List[int], minK: int, maxK: int) -> int:
        def solution_1697_5_2(arr):
            M=len(arr)
            minx=collections.deque()
            maxx=collections.deque()
            
            for i in range(M):
                if arr[i]==minK:
                    minx.append(i)
                    
                if arr[i]==maxK:
                    maxx.append(i)
                    
            total=0
            for i in range(M):
                while len(minx)>0 and minx[0]<i:
                    minx.popleft()
                    
                while len(maxx)>0 and maxx[0]<i:
                    maxx.popleft()
                    
                if len(minx)==0 or len(maxx)==0:
                    break
                    
                nx=max(minx[0],maxx[0])
                total+=M-nx
            return total
        total=0
        for g,t in groupby(nums,key=lambda x:minK<=x<=maxK):
            if g:
                total+=solution_1697_5_2(list(t))
        return total