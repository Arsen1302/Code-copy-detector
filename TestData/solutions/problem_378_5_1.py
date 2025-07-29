class Solution:
    def solution_378_5_1(self, n: int) -> int:
        def solution_378_5_2(currSteps: int, currChars: int, copiedChars: int) -> int:
            if currChars > n:  # Exceed.
                return float('inf')

            if currChars == n:  # Done.
                return currSteps

            if (currChars, copiedChars) not in memo:
                # Either copy all and paste or paste only.
                memo[(currChars, copiedChars)] = min(
                    solution_378_5_2(currSteps + 2, currChars << 1, currChars),
                    solution_378_5_2(currSteps + 1, currChars + copiedChars, copiedChars))

            return memo[(currChars, copiedChars)]

        if n == 1:
            return 0

        if n == 2:
            return 2

        memo = {}  # {(currChars, copiedChars): solution_378_5_1}.

        return solution_378_5_2(2, 2, 1)