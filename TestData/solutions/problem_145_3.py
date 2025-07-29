class Solution:
    def solution_145_3(self, secret: str, guess: str) -> str:
        unmatched_secret = [0] * 10
        unmatched_guess = [0] * 10
        bulls = 0
        for x, y in zip(secret, guess):
            x, y = int(x), int(y)
            if x == y:
                bulls += 1
            else:
                unmatched_secret[x] += 1
                unmatched_guess[y] += 1
        cows = sum(min(unmatched_secret[i], unmatched_guess[i]) for i in range(10))
        return f'{bulls}A{cows}B'