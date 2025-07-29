class Solution:
    def solution_1669_3_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        i, j = n - 1, n - 1
        bitCount = [0] * 32
        
        # add bits of k to bitCount
        def solution_1669_3_2(k):
            cnt = 0
            while k > 0:
                bitCount[cnt] += k &amp; 1
                k >>= 1
                cnt += 1
        
        # check if removing bits of k from bitCount decreases the current bitwise OR of numbers between i and j
        def solution_1669_3_3(k):
            cnt = 0
            while k > 0:
                if k &amp; 1 == 1 and bitCount[cnt] == 1:
                    return False
                k >>= 1
                cnt += 1
            return True
        
        # remove bits of k from bitCount
        def solution_1669_3_4(k):
            cnt = 0
            while k > 0:
                bitCount[cnt] -= (k &amp; 1)
                k >>= 1
                cnt += 1
        
        while i > -1:
            solution_1669_3_2(nums[i])
            while solution_1669_3_3(nums[j]) and i < j:
                solution_1669_3_4(nums[j])
                j -= 1
            i -= 1
            ret[i+1] = j - i
        
        return ret