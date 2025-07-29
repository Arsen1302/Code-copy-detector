class Solution:
    def solution_1437_5(self, nums: List[int], k: int) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort(reverse=True)

        arr = arr[:k]
        arr.sort(key=lambda k: k[1])

        return [val[0] for val in arr]