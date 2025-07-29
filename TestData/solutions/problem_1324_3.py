class Solution:
    def solution_1324_3(self, times: List[List[int]], targetFriend: int) -> int:
        n=len(times)
        times=[(a,l,idx) for idx,(a,l) in enumerate(times)]
        times.sort()
        available=list(range(n)) #available chair no
        used=[] #used chair (leaving,index)
        heapify(available)
        for a,l,i in times:
            while used and used[0][0]>=a:
                _,idx=heappop(used)
                heappush(available,idx)
            curr=heappop(available)
            if i==targetFriend:
                return curr
            heappush(used,curr)