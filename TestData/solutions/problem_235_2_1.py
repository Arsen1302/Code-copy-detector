class Solution:
    def solution_235_2_1(self, start: str, end: str, bank: list[str]) -> int:
        bank = set(bank) | {start}

        def solution_235_2_2(st0, cnt):
            if st0 == end:
                return cnt

            bank.remove(st0)
            for i, ch0 in enumerate(st0):
                for ch1 in "ACGT":
                    if (
                        ch0 != ch1
                        and (st1 := st0[:i] + ch1 + st0[i + 1 :]) in bank
                        and (res := solution_235_2_2(st1, cnt + 1)) != -1
                    ):
                        return res

            return -1

        return solution_235_2_2(start, 0)