class Solution:
    def solution_178_3(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        counter = counter1 &amp; counter2
        return list(counter.elements())