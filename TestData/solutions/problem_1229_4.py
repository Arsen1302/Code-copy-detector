class Solution:
    def solution_1229_4(self, s: str, knowledge: List[List[str]]) -> str:
        hashmap = collections.defaultdict(lambda: '?')
        for pair in knowledge:
            hashmap['(' + pair[0] + ')'] = pair[1]
        res = ''
        cur = ''
        flag = False
        for c in s:
            if flag:
                cur += c
                if c == ')':
                    res += hashmap[cur]
                    cur = ''
                    flag = False
            else:
                if c == '(':
                    flag = True
                    cur += c
                else:
                    res += c
        return res