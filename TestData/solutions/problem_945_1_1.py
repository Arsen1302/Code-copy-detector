class Solution:
    def solution_945_1_1(self, n: int) -> int:
        def solution_945_1_2(z):
            key = [1,1]
            while key[-1] + key[-2] <= z:
                key.append(key[-1]+key[-2])
            print(key,z)
            if z in key:
                return 1
            return 1 + solution_945_1_2(z-key[-1])
        return solution_945_1_2(n)