class Solution:
    def solution_693_5(self, arr: List[int]) -> bool:
        # sum of the array.
        total = sum(arr)
        # loop through the array.
        count = 0
        value = 0
        for i in arr:
            value += i
            if value == total/3 and count != 3:
                count += 1
                value = 0
        return True if count == 3 else False