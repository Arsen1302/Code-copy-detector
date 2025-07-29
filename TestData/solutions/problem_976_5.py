class Solution:
    def solution_976_5(self, sentence: str, searchWord: str) -> int:
        word_list = sentence.split(' ')

        for i in range(len(word_list)):
            if len(word_list[i]) >= len(searchWord):
                if word_list[i][0:len(searchWord)] == searchWord:
                    return i + 1
                continue

        return -1