class Solution:
    def solution_864_3(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)//2):
            answer += nums[2*i]*[nums[2*i+1]]
        return answer