class Solution:
    def solution_494_5(self, widths: List[int], s: str) -> List[int]:
        count, sum = 1, 0
        for i in s:
            a = widths[ord(i) - 97]
            sum += a
            if sum > 100:
                count += 1
                sum = a
        return [count, sum]