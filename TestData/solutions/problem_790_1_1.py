class Solution:
    def solution_790_1_1(self, s: str) -> str:
        def solution_790_1_2(string):
            n = len(string)
            word = ""
            i = 0
            while i <n:
                if string[i] == '(':
                    new = ""
                    count = 0
                    while True:
                        count += 1 if string[i] == '(' else -1 if string[i] == ')' else 0
                        if count == 0: break
                        new += string[i]
                        i += 1
                    i += 1
                    word += solution_790_1_2(new[1:])
                else:
                    word += string[i]
                    i += 1
            return word[::-1]
        return solution_790_1_2(s)[::-1]