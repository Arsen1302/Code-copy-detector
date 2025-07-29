class Solution:
    def solution_1487_4(self, nums: List[int]) -> List[int]:
        lst=[]
        dst=[]
        bst=[]
        mst=[]
        cst=[0]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                lst.append(nums[i])
                dst.append(i)
            else:
                bst.append(nums[i])
                mst.append(i)
        lst.sort()
        bst.sort()
        bst=bst[::-1]
        for i in range(len(lst)):
            cst[dst[i]]=lst[i]
        for j in range(len(bst)):
            cst[mst[j]]=bst[j]
        return cst