class Solution:
    def solution_406_2(self, nums: List[int], k: int) -> List[int]:
        rs0, rs1, rs2 = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        m0, m1, m2 = rs0, rs0 + rs1, rs0 + rs1 + rs2
        i0, i1, i2 = [0], [0, k], [0, k, 2*k]
        for i in range(len(nums)-3*k): 
            rs0 += nums[i+k] - nums[i]
            rs1 += nums[i+2*k] - nums[i+k]
            rs2 += nums[i+3*k] - nums[i+2*k]
            if rs0 > m0: m0, i0 = rs0, [i+1]
            if m0 + rs1 > m1: m1, i1 = m0 + rs1, i0 + [i+k+1]
            if m1 + rs2 > m2: m2, i2 = m1 + rs2, i1 + [i+2*k+1]
        return i2