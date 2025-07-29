class Solution:
    def solution_72_4(self, version1: str, version2: str) -> int:
        import itertools
        version1 = version1.split('.')
        version2 = version2.split('.')
        for v1, v2 in itertools.zip_longest(version1, version2, fillvalue=0):
            if int(v1)>int(v2):
                return 1
            elif int(v2)>int(v1):
                return -1
        return 0