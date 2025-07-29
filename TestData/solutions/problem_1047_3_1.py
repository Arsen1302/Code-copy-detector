class Solution:
    def solution_1047_3_1(self, positions, m, distance):
        current = positions[0] 
        ball = 1
        for position in positions:
            if position - current >= distance:
                current = position
                ball += 1
        return ball >= m


    def solution_1047_3_2(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left + 1 < right:
            mid = (left + right) // 2
            print(mid, left, right)
            if self.solution_1047_3_1(position, m, mid): 
                left = mid
            else:
                right = mid - 1
        return right if self.solution_1047_3_1(position, m, right) else left