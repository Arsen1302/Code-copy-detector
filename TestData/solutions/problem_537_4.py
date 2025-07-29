class Solution:
    def solution_537_4(self, seats: List[int]) -> int:
        seats = ''.join(map(str, seats))
        intervals = [len(x) for x in seats.split('1')]
        intervals[0] *= 2
        intervals[-1] *= 2
        return max((i + 1) // 2 for i in intervals)