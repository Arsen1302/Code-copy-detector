class Solution:
    def solution_1126_5(self, sequence: str, word: str) -> int:
        cnt = len(sequence)//len(word)
        repeat = word * cnt
        newstr = repeat + '#' + sequence
        lps = [0]
        maxi = 0
        for i in range(1, len(newstr)):
            x = lps[-1]
            while newstr[x] != newstr[i]:
                if x == 0:
                    x = -1
                    break
                x = lps[x-1]
            lps.append(x+1)
            if i>=len(repeat):
                maxi = max(maxi, x+1)
        return maxi//len(word)