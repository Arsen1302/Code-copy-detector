class Solution:
    def solution_592_4(self, nums: List[int], k: int) -> int:
        if len(set(nums)) == 1:
            return 0
        mini,maxi = min(nums),max(nums)
        if abs(mini - maxi) <=2*k:
            return 0
        else:
            return (maxi - k ) - (mini + k)