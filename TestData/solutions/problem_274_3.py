class Solution:
    def solution_274_3(self, nums: List[int], k: int) -> List[float]:
        window = OrderedList(nums[:k])
        medians = [window.median]
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            window.append(nums[i])
            medians.append(window.median)

        return medians