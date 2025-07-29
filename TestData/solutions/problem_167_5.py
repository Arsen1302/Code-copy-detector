class Solution:
    def solution_167_5(self, nums: List[int]) -> bool:
        least1=float('inf')
        least2=float('inf')
        for n in nums:
            if n<=least1:
                least1=n
            elif n<=least2:
                least2=n
            else:
                return True
        return False