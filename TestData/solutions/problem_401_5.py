class Solution:
    def solution_401_5(self, ops: List[str]) -> int:
        rec = []
        for i in ops:
            if i == 'C' and rec:
                rec.pop()
            elif i == 'D' and len(rec) >= 1:
                a = rec[-1]
                rec.append(2 * a)
            elif i == '+' and len(rec) >= 2:
                a = rec[-1]
                b = rec[-2]
                rec.append(b + a)
            else:
                rec.append(int(i))
        return sum(rec)