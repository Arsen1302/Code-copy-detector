class Solution:
    def solution_1232_2(self, sentence1: str, sentence2: str) -> bool:
        lst1, lst2 = sentence1.split(" "), sentence2.split(" ")
        for i, (a, b) in enumerate(zip(lst1, lst2)):
            if a != b:
                prefix = i
                break
        else:
            return True
        for i, (a, b) in enumerate(zip(lst1[::-1], lst2[::-1])):
            if a != b:
                suffix = i
                break
        else:
            return True
        return prefix + suffix in (len(lst1), len(lst2))