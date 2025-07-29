class Solution:
    def solution_1604_3(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [0]*len(nums1)
        s1,s2=0,0
        for i in range(len(nums1)):
            diff[i] = nums1[i]-nums2[i] 
            s1+=nums1[i]
            s2+=nums2[i]
        mneg,mpos,neg,pos = 0,0,0,0 
        for i in range(len(nums1)):
            neg+=diff[i]
            pos+=diff[i] 
            if neg>0:
                neg = 0 
            if pos<0:
                pos = 0 
            mpos = max(pos,mpos)
            mneg = min(neg,mneg)
        return max(s1-mneg,s2+mpos)