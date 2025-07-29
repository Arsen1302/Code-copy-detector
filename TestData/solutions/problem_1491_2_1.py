class Solution:
    def solution_1491_2_1(self, nums: List[int]) -> int:
        odd, even = Counter(), Counter()
        for i, x in enumerate(nums): 
            if i&amp;1: odd[x] += 1
            else: even[x] += 1
        
        def solution_1491_2_2(freq): 
            key = None
            m0 = m1 = 0
            for k, v in freq.items(): 
                if v > m0: key, m0, m1 = k, v, m0
                elif v > m1: m1 = v
            return key, m0, m1
        
        k0, m00, m01 = solution_1491_2_2(even)
        k1, m10, m11 = solution_1491_2_2(odd)
        return len(nums) - max(m00 + m11, m01 + m10) if k0 == k1 else len(nums) - m00 - m10