class Solution:
    def solution_998_4(self, names: List[str]) -> List[str]:
        ret, ret_set, name2nextSuffix = [], set(), {}
        for n in names:
            if n not in name2nextSuffix:
                ret.append(n)
                ret_set.add(n)
                name2nextSuffix[n] = 1
            else:
                suffix = name2nextSuffix[n]
                while n+'('+str(suffix)+')' in ret_set:
                    suffix += 1
                    name2nextSuffix[n] += 1
                name2nextSuffix[n] += 1
                name2nextSuffix[n+'('+str(suffix)+')'] = 1
                ret.append(n+'('+str(suffix)+')')                
        return ret