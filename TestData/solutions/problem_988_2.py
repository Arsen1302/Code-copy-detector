class Solution:
    def solution_988_2(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(n):
            l.extend([nums[i],nums[i+1]])
        return l