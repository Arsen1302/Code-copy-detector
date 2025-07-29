class Solution:
    def solution_365_1(self, nums: List[List[int]]) -> List[int]:
        k=len(nums)
        maxx=-float('inf')
        ans=[0,float('inf')]
        heap=[]
        for i in range(k):
            heap.append((nums[i][0],i,0))
            if nums[i][0]>maxx:maxx=nums[i][0]
        heapq.heapify(heap)
        while True:
            val,row,col= heapq.heappop(heap)
            tmp=maxx-val
            if tmp<ans[1]-ans[0]:ans=[val,maxx]
            elif tmp==ans[1]-ans[0] and val<ans[0]:ans=[val,maxx]
            if col+1==len(nums[row]):break        
            if nums[row][col+1]>maxx:maxx=nums[row][col+1]
            heapq.heappush(heap,(nums[row][col+1],row,col+1))
        return ans