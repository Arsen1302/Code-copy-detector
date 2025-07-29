class Solution:
    def solution_271_3(self, nums: List[int]) -> int:
        ans = 0
        freq = [0]*32 # count of "1" (32-bit "overkill")
        for k, x in enumerate(nums): 
            x = bin(x)[2:].zfill(32) # 32-bit binary  
            for i in range(32): 
                if x[i] == "0": ans += freq[i] # count of 1 
                else: # x[i] == "1"
                    ans += k - freq[i] # count of 0
                    freq[i] += 1 # update count 
        return ans