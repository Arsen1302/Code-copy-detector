class Solution:
    def solution_1030_4(self, target: str) -> int:
        '''
        Intuition: the min number of flips equals the number of toggles between 0 and 1 starting with 0.
        prev: previous character (0 at first)
        '''
        flips = 0
        prev = '0'
        for num in target:
            if num != prev:
                flips += 1
                prev = num
        return flips