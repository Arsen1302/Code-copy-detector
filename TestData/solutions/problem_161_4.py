class Solution:
    def solution_161_4(self, nums: List[int], lower: int, upper: int) -> int:
        # First get the cumulative list
        # takes O(n)
        accumulated = nums.copy()
        for i in range(0, len(nums)):
            if i != 0:
                accumulated[i] = nums[i] + accumulated[i-1]

        # sort the cumulative list
        # we do this because it's easy for later operations
        # takes O(n logn)
        new_acc = sorted(accumulated)

        result = 0
        num = 0

        # takes O(n)        
        for i in range(0, len(nums)):

            # get how many subarrays are within the bound
            # inside the loop, takes O(logn)
            l = bisect_left(new_acc, lower)
            r = bisect_right(new_acc, upper)
            diff = r - l

            result += diff
            lower += nums[num]
            upper += nums[num]
            poped = bisect_left(new_acc, accumulated[num])
            new_acc.pop(poped)
            num += 1

        # overall, takes O(n logn)
        return result