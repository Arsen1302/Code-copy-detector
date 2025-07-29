class Solution:
    def solution_873_3(self, s: str) -> List[str]:
        # split the words by spaces
        # find the longest word in s (how how elements in result array)
        # iterate through the words and add the characters to each row (to get column words)
        # use a pointer that indicates the position of the char in the word and the position to add the char into
        # the result array. If it's in bounds add the char otherwise add the space and increment
        # once done, iterate again and trim all leading spaces in the rows
        # time O(m * n) m = num of words n = word size O(n)


        words = s.split()
        maxlen = len(max(words, key=len))
        res = [""] * maxlen
        
        for word in words:
            i = 0
            while i < maxlen:
                if i < len(word):
                    res[i] += word[i]
                else:
                    res[i] += " "
                i += 1

        for i in range(maxlen):
            res[i] = res[i].rstrip()
        
        return res