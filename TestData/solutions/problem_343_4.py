class Solution:
    def solution_343_4(self, nums):
        n, sortedNums = len(nums), sorted(nums)
        mismatchArr = [a != b for a,b in zip(nums,sortedNums)]
        mismatchIdx = set(i for i,x in enumerate(mismatchArr) if x)
        diff = n - max(mismatchIdx, default=n) + min(mismatchIdx, default=n+1) - 1
        return n - diff