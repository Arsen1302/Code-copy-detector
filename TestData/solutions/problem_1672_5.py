class Solution:
    def solution_1672_5(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        counter = 1
        count_index = 0
        for i in range(len(s) - 1):
            if alphabet.index(s[i]) + 1 == alphabet.index(s[i + 1]):
                counter += 1
            else:
                if counter >=count_index:
                    count_index = counter
                    counter = 1
                else:
                    counter = 1
        return counter if counter > count_index else count_index