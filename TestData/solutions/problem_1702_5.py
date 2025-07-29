class Solution:
    def solution_1702_5(self, words: List[str]) -> str:
        # input: list of words with equal len
        # use ord(char) - 97 to get num for each char

        # then, we calculate each word element first through for loop
        # then we compare between each list element

        final_list = []

        for i in range(len(words)):
            diff_list = []
            for j in range(len(words[0]) - 1):
                diff_list.append(ord(words[i][j+1]) - ord(words[i][j]))

            final_list.append(diff_list)

        if str(final_list[0]) != str(final_list[1]):
            if str(final_list[0]) == str(final_list[2]):
                return words[1]
            elif str(final_list[1]) == str(final_list[2]):
                return words[0]

        else:
            for i in range(2, len(final_list)):
                if str(final_list[0]) != str(final_list[i]):
                    return words[i]