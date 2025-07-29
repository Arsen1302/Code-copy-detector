class Solution:
    def solution_220_4_1(self, nums: List[int], m: int) -> int:
        array = nums
        left, right = max(array), sum(array)

        while left < right:
            mid = (left + right) // 2
            if self.solution_220_4_2(array, mid, m):
                right = mid
            else:
                left = mid + 1


        return left



    def solution_220_4_2(self, array, mid, m):
        countSubArray = 1
        sumSubArray = 0

        for num in array:
            sumSubArray += num

            if sumSubArray > mid:
                sumSubArray = num
                countSubArray += 1
                if countSubArray > m:
                    return False


        return True