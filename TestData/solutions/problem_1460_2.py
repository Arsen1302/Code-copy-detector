class Solution:
    def solution_1460_2(self, title: str) -> str:
        title = title.split()
        word = []
        for i in range(len(title)):
            if len(title[i]) < 3:
                word.append(title[i].lower())
            else:
                word.append(title[i].capitalize())
        return " ".join(word)