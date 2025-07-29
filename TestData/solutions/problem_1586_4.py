class Solution:
    def solution_1586_4(self, password: str) -> bool:
        return len(password)>=8 \
					and any([c.isdigit() for c in password]) \
					and any([c.lower()!=c for c in password]) \
					and any([c.upper()!=c for c in password]) \
					and any([c in "!@#$%^&amp;*()-+" for c in password]) \
					and not any([password[i]==password[i+1] for i in range(len(password)-1)])