class Solution:
    def solution_625_5(self, strs: List[str]) -> int:
        length = len(strs[0])
        res= ''.join(strs)
        count =0
        for idx in range(length):
            index=idx
            while(index+length<len(res)):
                if(ord(res[index])>ord(res[index+length])):
                    count+=1
                    break
                index+=length
        return count