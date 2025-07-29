class Solution:
    def solution_519_2(self, s: str) -> str:
        if '@' in s:
            user,domain=s.split('@')
            return f'{user[0].lower()}{"*"*5}{user[-1].lower()}@{domain.lower()}'
        s=''.join([x for x in s if x.isdigit()])  ; n=0
        return f'+{"*"*(n-10)}-***-***-{s[-4:]}' if n>10 else f'***-***-{s[-4:]}'