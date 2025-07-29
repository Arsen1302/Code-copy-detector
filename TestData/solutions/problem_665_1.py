class Solution:
    # the idea is we don't calculate the even sum from scratch for each query
    # instead, we calculate it at the beginning
    # since each query only updates one value, 
    # so we can adjust the even sum base on the original value and new value
    def solution_665_1(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # calculate the sum of all even numbers
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []
        for val, idx in queries:
            # if original nums[idx] is even, then we deduct it from evenSum
            if nums[idx] % 2 == 0: evenSum -= nums[idx]
            # in-place update nums
            nums[idx] += val
            # check if we need to update evenSum for the new value
            if nums[idx] % 2 == 0: evenSum += nums[idx]
            # then we have evenSum after this query, push it to ans 
            ans.append(evenSum)
        return ans