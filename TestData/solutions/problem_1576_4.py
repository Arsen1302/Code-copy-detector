class Solution:
    def solution_1576_4(self, num: str) -> bool:
        d = Counter(num)
        for idx, val in enumerate(num):
            if int(val) != d[str(idx)]:
                return False
        return True