class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    def solution_816_4(self, sequences: List[str]) -> int:
        dp = [set()]

        for seq in sequences:
            chars = set(seq)

            if len(chars) < len(seq):
                continue

            dp.extend(chars | other for other in dp if not (chars &amp; other))

        return max(map(len, dp))