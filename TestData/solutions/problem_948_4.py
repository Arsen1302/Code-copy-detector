class Solution:
    def solution_948_4(self, s: str) -> str:

        # make a solution
        n = len(s)
        sol = [""]*(n+1)
        nr_pointer = 0
        chr_pointer = 1
        for char in s:
            if char.isdigit():
                if nr_pointer >= n:
                    return ""
                sol[nr_pointer] = char
                nr_pointer += 2
            else:
                if chr_pointer >= n+1:
                    return ""
                sol[chr_pointer] = char
                chr_pointer += 2
        
        # check the char pointer (whether there were)
        if chr_pointer == n+2:
            sol[-2] = sol[0]
            sol[0] = ""
        
        return "".join(sol)