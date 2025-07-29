class Solution:
    def solution_1604_4_1(self,arr):
        currSum,retval=[0]*2
        for i in range(len(arr)):
            currSum=max(currSum+arr[i],arr[i])
            retval=max(retval,arr[i],currSum)
        return retval
    def solution_1604_4_2(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        s1,s2=sum(nums1),sum(nums2)
        diff1,diff2=[],[]
        for i in range(n):
            diff1.append(nums2[i]-nums1[i])
        for i in range(n):
            diff2.append(nums1[i]-nums2[i])
        return max(s1+self.solution_1604_4_1(diff1),s2+self.solution_1604_4_1(diff2))