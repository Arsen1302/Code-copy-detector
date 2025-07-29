class Solution:
    def solution_961_4(self, nums: List[int], k: int) -> bool:
        x = int("".join(map(str, nums)), 2)
        return all((x &amp; (x << i)) == 0 for i in range(1, k+1))