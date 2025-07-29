class Solution:
    def solution_420_1(self, s: str) -> str:
        # Instead of using .lower(), let's implement with ASCII
        # ord() returns the ascii value of a passed character
        
        # Uncomment the line below to see the ASCII value of some important characters
        # print(ord('a'), ord('z'), ord('A'), ord('Z'))
        
        # Notice 'a'=97, and 'A'=65
        # This can be used to tell whether a character is upper/lower case, and can help us convert between them
        
        # First, make the string a list so we can change each char individually
        s = list(s)
        
        # Then, loop through the characters, and if their ascii value is <= 90 and >= 65, they must be upper case
        # Use the difference (97 - 65 = 32) to convert it from upper to lower, then use chr() to convert from ascii to char
        #   - ord('A') + 32 = 97 = ord('a')
        for i in range(len(s)):
            if ord(s[i]) <= 90 and ord(s[i]) >= 65:
                s[i] = chr(ord(s[i])+32)
        return ''.join(s)