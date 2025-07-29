class Solution:
    def solution_689_3(self, n: int) -> int:
        bin_n = bin(n)[2:]
        comp = "0b"
        for i in bin_n:
            if i == "0":
                comp += "1"
            else:
                comp += "0"
        return int(comp, 2)