class Solution:
    def solution_811_2(self, arr: List[str]) -> List[str]:
        arr.sort(key=len)
        
        files = []
        
        while arr:
            curr = arr.pop(0)
            temp = []
            for i in arr:
                if(curr + '/' in i and i.index(curr + '/') == 0):
                    pass
                else:
                    temp.append(i)
            
            files.append(curr)
            arr = temp
        
        return files