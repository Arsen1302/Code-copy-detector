class Solution:
    def solution_892_2(self, arr: List[int]) -> bool:
        hashMap = {}
        for i in arr:
            if(hashMap.get(i+i)):
                return True
            if(i%2 == 0 and hashMap.get(i//2)):
                return True
            hashMap[i] = True
        return False