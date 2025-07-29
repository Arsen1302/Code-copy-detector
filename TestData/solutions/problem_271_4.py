class Solution:
    def solution_271_4(self, nums: List[int]) -> int:
        
        # bits stores the count of numbers in nums for which the ith bit is set
        
        bits = [0]*32
        
        # consider [4,14,2]
        # 
        #   3 2 1 0 (ith bit)
        # ---------------
        #   0 1 0 0 -> 4 
        #   1 1 1 0 -> 14
        #   0 0 1 0 -> 2
        # ---------------
        #   1 2 2 0 -> bits[]
        #
        # if the ith bit of a number is zero then 
        # the sum of its XOR at ith bit with every number in nums will be bits[i] 
    
        
        for num in nums:
            i = 0
            while num:
                bits[i] += num&amp;1
                num = num >>1
				i+=1
        
        total = 0
        for num in nums:
            for i in range(32):
                if not num&amp;1:
                    total += bits[i]
                num = num >>1
             
        return total


# UPDATE: 
        
        ans = 0
        n = len(nums)
        
        # the sum of pair wise XOR at ith bit is
        # the product of number of set bits and unset bits
        
        
        for i in range(32):
            ones = 0
            for num in nums:
                ones += (num>>i)&amp;1
            # (n - ones) is the number of zeroes
            ans += ones*(n-ones)
        return ans