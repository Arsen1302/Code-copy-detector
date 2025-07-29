class Solution:
#     O(n) || O(1)
    def solution_589_3(self, array: List[int]) -> List[int]:
        if not array: return array
        left, right = 0, len(array) - 1

        while left < right:
            if array[left] % 2 == 0:
                left += 1
            else:
                array[left], array[right] = array[right], array[left]
                right -= 1

        return array