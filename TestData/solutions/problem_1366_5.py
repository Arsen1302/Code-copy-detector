class Solution:
#     Runtime: 37ms 78.98% || Memory: 13.8mb 65.61%
    def solution_1366_5(self, string: str, letter: str) -> str:
        newString = list(string)

        for idx, val in enumerate(newString):
            if val == letter:
                newString[:idx+1] = newString[:idx+1][::-1]
                return ''.join(newString)

        return ''.join(newString)