class Solution:
    def solution_509_3(self, S: str, C: str) -> List[int]:
        l = [0] * len(S)
        prev = None
        for i, x in enumerate(S):
            if x == C:

				# only correct the closer half of the indexes between previous and current if previous is not None
                start = 0 if prev is None else (i + prev) // 2 + 1

				# slice assign where corrections are needed to a range
                l[start:i + 1] = range(i - start, -1, -1)

                prev = i
            elif prev is not None:
                l[i] = i - prev
        return l