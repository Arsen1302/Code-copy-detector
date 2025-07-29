class Solution:
    def solution_1290_4(self, chalk: List[int], k: int) -> int:
		return bisect.bisect(list(accumulate(chalk)), k % sum(A))