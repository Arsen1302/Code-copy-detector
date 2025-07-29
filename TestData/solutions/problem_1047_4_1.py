class Solution:
    def solution_1047_4_1(self, position: List[int], m: int) -> int:

        position.sort()
        def solution_1047_4_2(force):
            res = 1
            start = position[0]
            for i in range(1, len(position)):
                if position[i] - start >= force:
                    res += 1
                    start = position[i]
            return res

        left, right = 1, position[-1] -  position[0]
        while left < right:
            mid = left + (right - left + 1) // 2
            if solution_1047_4_2(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left