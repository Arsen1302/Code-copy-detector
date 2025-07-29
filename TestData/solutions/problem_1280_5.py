class Solution:
    def solution_1280_5(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        target_val = 0

        temp = ""
        for i in targetWord:
            temp += str(alphabets.index(i))
        target_val = int(temp)

        temp = ""
        for i in firstWord:
            temp += str(alphabets.index(i))
        target_val -= int(temp)

        temp = ""
        for i in secondWord:
            temp += str(alphabets.index(i))
        target_val -= int(temp)

        if target_val:
            return False
        else:
            return True