class Solution:
#     O(n) || O(26)
# Runtime: 40ms 78.04% memory: 14.2mb 60.39%
    def solution_546_2(self, string: str, goal: str) -> bool:
        left, right = 0, len(string) - 1

        if len(string) != len(goal):
            return False

        if string == goal and len(set(string)) < len(string):
            return True


        difference = []

        for i in range(len(string)):
            if string[i] != goal[i]:
                difference.append((string[i], goal[i]))


        if len(difference) == 2 and difference[0] == difference[-1][::-1]: 
            return True


        return False