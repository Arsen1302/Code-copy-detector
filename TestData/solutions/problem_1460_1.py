class Solution:
    def solution_1460_1(self, title: str) -> str:
        title = title.split()
        word = ""
        for i in range(len(title)):
            if len(title[i]) < 3:
                word = word + title[i].lower() + " "
            else:
                word = word + title[i].capitalize() + " "
        return word[:-1]