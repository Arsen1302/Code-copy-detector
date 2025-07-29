class Solution:
    def solution_1586_3(self, ps: str) -> bool:
        ln = len(ps) >= 8
        lower = False
        upper = False
        dig = False
        spec = False
        spec_symb = "!@#$%^&amp;*()-+"
        not_adj = True
        for i in ps:
            if i.islower():
                lower = True
            if i.isupper():
                upper = True
            if i.isdigit():
                dig = True
            if i in spec_symb:
                spec = True
        for i in range(1, len(ps)):
            if ps[i] == ps[i-1]:
                not_adj = False
        return ln == lower == upper == dig == spec == not_adj