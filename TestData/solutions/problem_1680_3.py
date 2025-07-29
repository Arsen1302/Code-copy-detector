class Solution:
    def solution_1680_3(self, nums1: List[int], nums2: List[int]) -> int:
#         nums3 = []
#         for n1 in nums1:
#             for n2 in nums2:
#                 nums3.append(n1 ^ n2)
                
#         ans1 = 0
#         for i in range(len(nums3)):
#             ans1 = ans1 ^ nums3[i]
        
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        if n2%2==1:
            for i in range(n1):
                ans = ans ^ nums1[i]
        
        if n1%2==1:
            for i in range(n2):
                ans = ans ^ nums2[i]
        
        # print(ans1, ans)
        return ans