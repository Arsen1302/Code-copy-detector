class Solution:
    #O(n) traverse
    #O(1) space
    def solution_1352_2_1(self, nums: List[int]) -> List[int]:
        min, max = nums[0], nums[0]
        for num in nums:
            if max < num: max = num
            if min > num: min = num
        return [max,min]

    #Euclidian solution_1352_2_2
    #constraint: a>b
    #O(h) where h is number of digits in (smaller number) b
    #O(1) space
    def solution_1352_2_2(self, ints: List[int]) -> int:
        a,b = ints[0], ints[1]
        while ((a % b) > 0):
            remainder = a % b
            a = b
            b = remainder
        return b

    # 2 <= nums.length <= 1000
    # 1 <= nums[i] <= 1000
    # O(h+n) = O(n)
    # O(n) space with nums inside
    def solution_1352_2_3(self, nums: List[int]) -> int:
        return self.solution_1352_2_2(self.solution_1352_2_1(nums))