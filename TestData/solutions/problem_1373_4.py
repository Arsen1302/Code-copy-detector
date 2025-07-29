class Solution:
def solution_1373_4(self, nums: List[int]) -> int:
    
    n=len(nums)
    nums = sorted(set(nums))
    res = n
    for i,st in enumerate(nums):
        end = st+n-1
        ind = bisect.bisect_right(nums,end)
        unq_len = ind-i
        res = min(res,n-unq_len)
    return res