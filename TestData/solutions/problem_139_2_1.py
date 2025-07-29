class Solution:
    def solution_139_2_1(self, num, target, ind, l, mem, exp):
        if ind == l - 1:
            exp += num[ind]
            if eval(exp) == target:
                return [exp]
        if ind >= l:
            return []
        ret1 = self.solution_139_2_1(num, target, ind + 1, l, mem, exp + str(num[ind]) + '+')
        ret2 = self.solution_139_2_1(num, target, ind + 1, l, mem, exp + str(num[ind]) + '-')
        ret3 = self.solution_139_2_1(num, target, ind + 1, l, mem, exp + str(num[ind]) + '*')
        if (exp and exp[-1].isdigit() is True and num[ind] == '0') or num[ind] != '0':
            ret4 = self.solution_139_2_1(num, target, ind + 1, l, mem, exp + str(num[ind]))
            ret = ret1 + ret2 + ret3 + ret4
        else:
            ret = ret1 + ret2 + ret3
        return ret
        
    def solution_139_2_2(self, num: str, target: int) -> List[str]:
        return self.solution_139_2_1(num, target, 0, len(num), dict(), '')