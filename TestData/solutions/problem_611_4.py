class Solution:
    def solution_611_4(self, emails):
        s = set()
        for i in emails:
            a, b = i.split('@')
            if '+' in a:
                a = a[:a.index('+')]
            s.add(a.replace('.','') + '@' + b)
        return len(s)