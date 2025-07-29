class Solution:
    def solution_194_5(self, ransomNote: str, magazine: str) -> bool:
        dict1=collections.Counter(ransomNote)
        dict2=collections.Counter(magazine)
        for key in dict1:
            if key not in dict2 or dict2[key]<dict1[key]:
                return False
        return True