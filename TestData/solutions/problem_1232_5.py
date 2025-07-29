class Solution:
    def solution_1232_5(self, sentence1: str, sentence2: str) -> bool:
        sentence1, sentence2 = sentence1.split(), sentence2.split()
        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1
        for p in range(len(sentence2)):
            if sentence1[p] != sentence2[p]:
                return sentence1[-(len(sentence2) - p):] == sentence2[p:]
        return True