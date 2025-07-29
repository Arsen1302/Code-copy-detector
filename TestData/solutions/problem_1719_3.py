class Solution:
    def solution_1719_3(self, nums: list[int], k: int) -> int:
        coprime_count = 0

        for subarray_end, n in enumerate(nums):
            nums[subarray_end] = k // n if k % n == 0 else None
            running_gcd = 0

            for subarray_start in reversed(range(subarray_end + 1)):
                if not nums[subarray_start]:
                    break

                running_gcd = gcd(running_gcd, nums[subarray_start])
                coprime_count += running_gcd == 1

        return coprime_count