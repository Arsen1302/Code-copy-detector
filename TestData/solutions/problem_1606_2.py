class Solution:
    def solution_1606_2(self, key: str, message: str) -> str:
        char_map = {' ': ' '}
        
        for char in key:
            if char not in char_map:
                char_map[char] = chr(ord('a') + len(char_map) - 1)
        
        return ''.join([char_map[char] for char in message])