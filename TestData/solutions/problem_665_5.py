class Solution:
    def solution_665_5(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        cur_sum=sum([i for i in nums if not i%2])
        for q in queries:
            if not nums[q[1]]%2:
                cur_sum-=nums[q[1]]
            nums[q[1]]+=q[0]
            if not nums[q[1]]%2:
                cur_sum+=nums[q[1]]
            res.append(cur_sum)
        return res