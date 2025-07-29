class Solution(object):
    def solution_194_2(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 &amp; st2 == st1:
            return True
        return False