class Solution:
    def solution_271_2(self, nums: List[int]) -> int:
        freq = [0]*32 # count of "1" (32-bit "overkill")
        for x in nums: 
            x = bin(x)[2:].zfill(32) # 32-bit binary  
            for i in range(32): freq[i] += x[i] == "1"  # count of 1 
        return sum(freq[i] * (len(nums) - freq[i]) for i in range(32))