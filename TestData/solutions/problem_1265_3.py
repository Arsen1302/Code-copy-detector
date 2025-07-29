class Solution:
    def solution_1265_3(self, s: str) -> str:
        word_list = s.split()  # form a list of words
        n = len(word_list)  # total words in the list, at max 9
        
		# dict to make k, v pairs as there are at max 9 words in the array
		# key as position of word, value as word without position
		# because while joining, fetching from dict will take constant time
		# and we can just add values iterating over keys from 1 to 9 (including)
		index_dict = dict()  
        for word in word_list:
            index_dict[int(word[-1])] = word[:-1]

        res = ""
		# iterate from 1 to n, and add up all the values
        for i in range(1, n+1):
            res += index_dict.get(i, "")
            res += " "
			
		# we can alse use, res[:-1], res.strip()
        return res.rstrip()  # right strip as " " is present at the end of the sentence