class Solution:
    def solution_1101_4(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        main=[]
        for i in range(len(l)):
            l1=(nums[l[i]:r[i]+1])
            mi = min(l1)
            ma=max(l1)
            check=(ma-mi)//(len(l1)-1)
            x=mi
            while(x<ma):
                if x not in l1:
                    main.append(False)
                    break
                l1.remove(x)    
                x+=check
            if(x==ma):    
                main.append(True)
        return main