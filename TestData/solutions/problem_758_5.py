class Solution:
    def solution_758_5(self, hours: List[int]) -> int:
        prefixSum=0
        hmap=defaultdict(int)
        ans=0
        for length,hour in enumerate(hours):
            prefixSum+=1 if hour>8 else -1
            if prefixSum>0:ans=max(ans,length+1)
            if prefixSum not in hmap:
                hmap[prefixSum]=length
            if prefixSum-1 in hmap:
                ans=max(ans,length-hmap[prefixSum-1])
        return ans