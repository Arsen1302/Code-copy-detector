class Solution:
    def solution_145_5(self, secret: str, guess: str) -> str:
        Bulls,Cows, Position = 0,0, []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                Bulls += 1
                Position.append(i)
        for i in range(len(Position)):
            idx = Position[i] - i
            secret = secret[:idx] + secret[idx+1:]
            guess = guess[:idx] + guess[idx+1:]
        for i in range(len(guess)):
            if guess[i] in secret:
                Cows += 1
                idx = secret.index(guess[i])
                secret = secret[:idx] + secret[idx+1:]
        return str(Bulls)+"A"+str(Cows)+"B"