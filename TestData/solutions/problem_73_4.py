class Solution:
    def solution_73_4(self, numerator: int, denominator: int) -> str:
        pre = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        q = str(q)
        if r == 0:
            return pre + q
        res = pre + q + "."
        dic = {}
        idx = len(res)
        r *= 10
        while r > 0:
            if r in dic:
                return res[:dic[r]] + f"({res[dic[r]:]})"
            dic[r] = idx
            q, r = divmod(r, denominator)
            res += (q := str(q))
            if r == 0:
                return res
            idx += len(q)
            r *= 10