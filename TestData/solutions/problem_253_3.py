class Solution:
    def solution_253_3(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ht = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                ht[n1 + n2] += 1
        ans = 0
        c=0
        for n3 in nums3:
            for n4 in nums4:
                c=ht[-n3 - n4]
                ans +=c
        return ans