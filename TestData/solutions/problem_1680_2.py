class Solution:
    def solution_1680_2(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)%2
        n2 = len(nums2)%2

        n1xor = 0 
        n2xor = 0 
        
        if n2 == 1:
            for n in nums1:
                n1xor ^= n
        
        if n1 == 1:
            for n in nums2:
                n2xor ^= n      

        return n1xor ^ n2xor