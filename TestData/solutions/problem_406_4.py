class Solution:
    def solution_406_4(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s0 = sum(nums[:k]) # sum of the first subarray
        r0 = [s0, 0] # max of the first subarray and its starting index
        s1 = sum(nums[k:(2*k)]) # sum of the second subarray
        r1 = [r0[0]+s1, 0, k] # max of the sum of the first two subarrays and their starting indices
        s2 = sum(nums[(2*k):(3*k)]) # sum of the third subarray
        r2 = [r1[0]+s2, 0, k, 2*k] # max of the sum of all three subarrays and their starting indices
        idx = [1, k+1, 2*k+1]
        while idx[2] < n-k+1: # using a sliding window approach
            s0 += nums[idx[0]+k-1] - nums[idx[0]-1]
            # find the max of the first one, two, three subarrays by turn
            if s0 > r0[0]:
                r0 = [s0, idx[0]]
            s1 += nums[idx[1]+k-1] - nums[idx[1]-1]
            if s1 + r0[0] > r1[0]:
                r1 = [s1+r0[0], r0[1], idx[1]]
            s2 += nums[idx[2]+k-1] - nums[idx[2]-1]
            if s2 + r1[0] > r2[0]:
                r2 = [s2+r1[0], r1[1], r1[2], idx[2]]
            idx[0] += 1
            idx[1] += 1
            idx[2] += 1
        return [r2[1], r2[2], r2[3]]