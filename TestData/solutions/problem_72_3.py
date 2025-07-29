class Solution(object):
    def solution_72_3(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        c = 0
        while c < len(version1) and c < len(version2):
            if int(version1[c])>int(version2[c]):
                return 1
            elif int(version2[c])>int(version1[c]):
                return -1
            else:
                c += 1
        if c < len(version1):
            for i in version1[c:]:
                if int(i) > 0:
                    return 1
        if c < len(version2):
            for i in version2[c:]:
                if int(i) > 0:
                    return -1
        return 0