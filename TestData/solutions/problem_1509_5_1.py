class Solution:
    def solution_1509_5_1(self, s: str) -> int:
        ans = 0

        def solution_1509_5_2(current: str) -> str:
            nonlocal ans
            left, right = dict(), dict()
            len_c1 = len(current) - 1
            for i, c in enumerate(current):
                if c in right and i != right[c]:
                    j = right[c]
                    i, j = (i, j) if i < j else (j, i)
                    ans += i + len_c1 - j
                    return f"{current[:i]}{current[i + 1:j]}{current[j + 1:]}"
                elif c not in left:
                    left[c] = i
                j = len_c1 - i
                right_c = current[j]
                if right_c in left and left[right_c] != j:
                    i = left[right_c]
                    i, j = (i, j) if i < j else (j, i)
                    ans += i + len_c1 - j
                    return f"{current[:i]}{current[i + 1:j]}{current[j + 1:]}"
                elif right_c not in right:
                    right[right_c] = j

            return ""

        while len(s) > 2:
            s = solution_1509_5_2(s)

        return ans