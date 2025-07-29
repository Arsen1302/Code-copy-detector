class Solution:
    def solution_1604_5(self, nums1: List[int], nums2: List[int]) -> int:
        # Double Kadane
        # T(c)=O(n)
        # Either replace nums from arr1 or from arr2
        # Then find maximum
        n=len(nums1)
        msfar1=0
        msfar2=0
        k_sum1=0
        k_sum2=0
        for i in range(n):
            msfar1+=nums2[i]-nums1[i]
            k_sum1=max(msfar1,k_sum1)
            msfar2+=nums1[i]-nums2[i]
            k_sum2=max(msfar2,k_sum2)
            
            if msfar1<0:
                msfar1=0
            if msfar2<0:
                msfar2=0
        return max(sum(nums1)+k_sum1,sum(nums2)+k_sum2)