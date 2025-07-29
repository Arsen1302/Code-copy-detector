class Solution:
    def solution_519_3(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, rest = s.split('@')
            name = name[0] + '*****' + name[-1]
            return name + '@' + rest
        else:
            num = ''.join([n for n in s if n in '1234567890'])
            if len(num) == 10:
                return "***-***-" + num[-4:]
            elif len(num) == 11:
                return "+*-***-***-" + num[-4:]
            elif len(num) == 12:
                return "+**-***-***-" + num[-4:]
            else:
                return "+***-***-***-" + num[-4:]