class Solution:
    def solution_448_5(self, licensePlate: str, words: List[str]) -> str:
        
        # Runtime: 64 ms, faster than 93.88%
        # Memory Usage: 14.5 MB, less than 81.41%
        
        words = sorted(words, key=len)  # Handle multiple shortest 'completing' words
        lic = ''.join(sorted([x for x in licensePlate.lower() if 96 < ord(x) <= 122]))

        for word in words:
            
            buff = ''.join(word)
            exists = True
            for char in lic:
                if char not in buff:
                    exists = False
                    break
                else:
                    if buff.count(char) < lic.count(char):
                        exists = False
                        break
            if exists:
                return word