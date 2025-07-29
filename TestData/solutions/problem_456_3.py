class Solution:
    def solution_456_3(self, left: int, right: int) -> int:
        set_ = {2, 3, 5, 7, 11, 13, 17, 19}
        h = 0
        for  i in range(left, right + 1):
            w = bin(i)
            count = w.count("1")
            if count in set_:
                h += 1
        return h