class Solution:
    def solution_756_3(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        temp = []
        
        for i in arr2:
            count = arr1.count(i)

            while count > 0:
                result.append(i)
                count -= 1

        for i in arr1:
            if i not in arr2:
                temp.append(i)

        result += sorted(temp)
        
        return result