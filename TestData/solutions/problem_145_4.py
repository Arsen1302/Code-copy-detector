class Solution:
    def solution_145_4(self, secret: str, guess: str) -> str:
        dict1 = {}
        cows = bulls = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in dict1:
                    dict1[secret[i]] = 1
                else:
                    dict1[secret[i]] += 1

        for i in range(len(guess)):
            if guess[i] in dict1 and secret[i] != guess[i]:
                if dict1[guess[i]] > 0:
                    dict1[guess[i]] -=1
                    cows+=1

        return f"{bulls}A{cows}B"