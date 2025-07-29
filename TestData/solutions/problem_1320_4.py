class Solution:
    def solution_1320_4(self, text: str, brokenLetters: str) -> int:
        s=[]
        text=text.split()
        for i in text:
            for j in i:
                if j in brokenLetters:
                    break
            else:
                s.append(i)
        return len(s)