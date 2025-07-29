class Solution:
    def solution_988_1(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(n):
            l.append(nums[i])
			l.append(nums[n+i])
        return l