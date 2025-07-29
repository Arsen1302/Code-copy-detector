class Solution:
    def solution_253_4(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        n=len(nums1)
        res=0
        d1=defaultdict(int)
        d2=defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                d1[nums1[i]+nums2[j]]+=1
        
        for i in range(n):
            for j in range(n):
                d2[nums3[i]+nums4[j]]+=1
        
        for key in d1:
            res+=(d1[key]*d2[-key])
        
        return res
		
		# Please upvote if you find this solution useful :)