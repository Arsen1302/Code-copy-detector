class Solution:
    def solution_423_5(self, nums: List[int], k: int) -> int:

        result = 0
        product = 1
        lagging = 0

        for leading in range(len(nums)):
            product *= nums[leading]
            
            while product >= k and lagging <= leading:
                product /= nums[lagging]
                lagging += 1
                
            sub_arr_len = leading - lagging + 1
            result += sub_arr_len

        return result