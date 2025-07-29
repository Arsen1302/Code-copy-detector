class Solution:
    def solution_1265_2(self, s: str) -> str:
		# split the string and sort the words based upon the last letter
        word_list = sorted(s.split(), key = lambda word: word[-1], reverse = False)
        return " ".join([word[:-1] for word in word_list])  # join the words, after removing the last letter ie., digit