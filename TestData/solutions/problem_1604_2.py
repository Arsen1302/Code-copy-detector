class Solution:
    def solution_1604_2(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = [0]*n
        for i in range(n):
            diff[i] = nums1[i]-nums2[i]
        mpos,mneg,pos,neg = 0,0,0,0
        for i in range(n):
            pos += diff[i]
            if pos < 0:
                pos = 0
            neg += diff[i]
            if neg > 0:
                neg = 0
            mpos = max(pos,mpos)
            mneg = min(neg,mneg)
        return max(sum(nums1)-mneg,sum(nums2)+mpos)