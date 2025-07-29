class Solution:
    def solution_961_2(self, nums: List[int], k: int) -> bool:
        indices = [i for i,x in enumerate(nums) if x==1]
        return all([indices[i+1]-indices[i]>k for i in range(len(indices)-1)])