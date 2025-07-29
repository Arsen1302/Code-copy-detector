class Solution:
    def solution_1320_3(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        flag = 0
        for i in words:
            for j in brokenLetters:
                if j in i:
                    flag = 1
                    break
            if flag == 0:
                count += 1
            flag = 0
        return count