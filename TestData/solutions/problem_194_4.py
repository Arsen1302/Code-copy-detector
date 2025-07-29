class Solution:
    def solution_194_4(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote)-Counter(magazine)=={}