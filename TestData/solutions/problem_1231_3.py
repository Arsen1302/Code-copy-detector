class Solution:
    def solution_1231_3(self, coordinates: str) -> bool:
        return True if ((ord(coordinates[0]))+int(coordinates[1])) % 2 else False