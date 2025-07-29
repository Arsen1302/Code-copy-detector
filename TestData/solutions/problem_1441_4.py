class Solution:
    def solution_1441_4(self, nums: List[int]) -> int:
        
        # Reference: https://cybergeeksquad.co/2022/02/shipment-imbalance-amazon-oa.html#SOLUTION
        # count number of times each number is used as a maximum and minimum
        
        gl = [None] * len(nums) # greater left
        gr = [None] * len(nums) # greater right
        ll = [None] * len(nums) # lesser left
        lr = [None] * len(nums) # lesser right
        
        s = [(0, math.inf)]
        for i in range(len(nums)):
            while len(s) != 0 and s[-1][-1] < nums[i]:
                s.pop()
            s.append((i+1, nums[i]))
            gl[i] = s[-1][0] - s[-2][0]
            
        s = [(len(nums), math.inf)]
        for i in range(len(nums)-1, -1, -1):
            while len(s) != 0 and s[-1][-1] <= nums[i]:
                s.pop()
            s.append((i, nums[i]))
            gr[i] = s[-2][0] - s[-1][0]

        s = [(0, -math.inf)]
        for i in range(len(nums)):
            while len(s) != 0 and s[-1][-1] > nums[i]:
                s.pop()
            s.append((i+1, nums[i]))
            ll[i] = s[-1][0] - s[-2][0]
            
        s = [(len(nums), -math.inf)]
        for i in range(len(nums)-1, -1, -1):
            while len(s) != 0 and s[-1][-1] >= nums[i]:
                s.pop()
            s.append((i, nums[i]))
            lr[i] = s[-2][0] - s[-1][0]
            
        g = [gl[i]*gr[i] for i in range(len(nums))] # number of times nums[i] is maximum
        l = [ll[i]*lr[i] for i in range(len(nums))] # number of times nums[i] is minimum
        
        return sum([(g[i]-l[i])*nums[i] for i in range(len(nums))])