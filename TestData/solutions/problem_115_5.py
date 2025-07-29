class Solution:
    def solution_115_5(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        c = Counter(nums)
        fin = []
        for key, val in c.items():
            if val > limit:
                fin.append(key)
        return fin