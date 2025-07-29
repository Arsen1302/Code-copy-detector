class Solution:
    def solution_5_4(self, s: str) -> str:
        """
        Consider each character in s as the centre of a palindrome.
        Check for the longest possible odd-length and even-length palindrome; store the longest palindrome
        """
        # res is the starting index of the longest palindrome
        # len_res is the length of the longest palindrome
        # len_s is the length of the given string
        res, len_res, len_s = 0, 0, len(s)
        for i in range(len_s):
            # check for palindromes with odd number of characters centred around s[i]
            # i.e., s[i] -> s[i-1:i+2] -> s[i-2:i+3] -> ...
            # odd is the starting index of the current palindrome with odd number of characters
            # len_odd is the length of the current palindrome with odd number of characters
            odd, len_odd = i, 1
            for j in range(min(i, len_s-i-1)):   # checking indexes [0, i) and [i+1, len_s); take the smaller range
                if s[i-j-1] != s[i+j+1]:         # if the two characters adjacent to the ends of the current palindrome are not equal,
                    break                        #   a longer palindrome does not exist; break out of the loop
                odd, len_odd = odd-1, len_odd+2  # else, a longer palindrome exists; update odd and len_odd to point to that palindrome
            # check for palindromes with even number of characters centred around s[i-1:i+1]
            # i.e., s[i-1:i+1] -> s[i-2:i+2] -> s[i-3:i+3] -> ...
            # even is the starting index of the current palindrome with even number of characters
            # len_even is the length of the current palindrome with even number of characters
            even, len_even = i, 0
            for j in range(min(i, len_s-i)):         # checking indexes [0, i) and [i, len_s); take the smaller range
                if s[i-j-1] != s[i+j]:               # if the two characters adjacent to the ends of the current palindrome are not equal,
                    break                            #   a longer palindrome does not exist; break out of the loop
                even, len_even = even-1, len_even+2  # else, a longer palindrome exists; update even and len_even to point to that palindrome
            # update res and len_res to point to the longest palindrome found so far
            len_res, res = max((len_res, res), (len_odd, odd), (len_even, even))
        return s[res:res+len_res]