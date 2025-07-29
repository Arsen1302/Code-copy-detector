class Solution:
    def solution_91_5(self, n: int) -> bool:
        if n == 1:
            return True
        seen = {}
        while n != 1:
            sqa_summed = sum([(int(i) ** 2) for i in str(n)])
            if sqa_summed not in seen:
                seen[sqa_summed] = sqa_summed
                n = sqa_summed
            else:
                return False

        return True