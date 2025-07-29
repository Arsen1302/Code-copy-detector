class Solution:
    def solution_811_5(self, folder):
        result = []

        for i in sorted(folder):
            if not result or not i.startswith(result[-1] + "/"):
                result.append(i)

        return result