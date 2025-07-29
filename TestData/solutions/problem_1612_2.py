class Solution:
    def solution_1612_2(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        differences = [ abs(x - y) for x, y in zip(nums1, nums2)]
        
        if sum(differences) <= k1 + k2:
            return 0
        
        if k1 + k2 == 0:
            return sum([x**2 for x in differences])
        
        diff = defaultdict(int)
        for num in differences:
            diff[num] += 1
        
        total = k1 + k2
        maxK = max(diff.keys())
        for k in range(maxK, 0, -1):
            if diff[k] > 0:
                temp = min(total, diff[k])
                diff[k] -= temp
                diff[k - 1] += temp
                total-= temp
        
        res = 0

        for k, v in diff.items():
            res += (v * (k **2))
        
        return res