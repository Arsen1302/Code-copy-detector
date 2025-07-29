class Solution:
    def solution_724_1(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # we need to insert the remaining stone (s1-s2) into the list
                pass
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain