class Solution:
    def solution_1511_2(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        nums.insert(0, 0)
        nums.append(2000000001)
        n = len(nums)
        for i in range(n-1):
            start = nums[i] # This is the lowerbound for current iteration
            end = nums[i+1] # This is the higherbound for current iteration
            if start == end:
                continue
            a = start + 1 # Starting value is lowerbound + 1
            n = min(end - start - 1, k) # Since the total number possible b/w start and end might be more than the k numbers left, so always choose the minimum.
            v = (n*(2*a + n - 1))//2 # n/2[2a + (n-1)d] with d = 1
            res += v # Add the sum of elements selected into res
            k -= n # n number of k's expired, thus k decrements
        return res