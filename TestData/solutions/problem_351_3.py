class Solution:
    def solution_351_3(self, nums: List[int]) -> int:
        C=Counter(nums) ; mx=0
        for i in C:
            if i+1 in C: mx=max(C[i]+C[i+1],mx)
        return mx