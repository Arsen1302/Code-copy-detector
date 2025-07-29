class Solution:
#     O(n) || O(1)
# Runtime: 47ms 64.61% || Memory: 13.7mb 97.39%
    def solution_1598_2(self, string: str) -> int:
        if not string:
            return 0

        isBetweenBar = False

        asteriskCount = 0

        for char in string:
            if char == '|' and not isBetweenBar:
                isBetweenBar = True

            elif char == '|' and isBetweenBar:
                isBetweenBar = False

            if not isBetweenBar and char == '*':
                asteriskCount += 1

        return asteriskCount