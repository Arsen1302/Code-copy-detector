class Solution:
    def solution_519_4(self, s: str) -> str:
        if '@' in s:
            user, domain = s.split('@')
            return f'{user[0].lower()}{"*"*5}{user[-1].lower()}@{domain.lower()}'
        else:
            s = ''.join([c for c in s if c.isdigit()])
            n = len(s)    
            return f'+{"*"*(n-10)}-***-***-{s[-4:]}' if n != 10 else f'***-***-{s[-4:]}'