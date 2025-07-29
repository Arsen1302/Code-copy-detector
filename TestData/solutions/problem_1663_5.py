class Solution:
    def solution_1663_5(self, nums: List[int]) -> int:
        ccc = collections.Counter(nums)
        mxe=-1
        mx=0
        for i in ccc.keys():
            if ccc[i]>mx and i%2==0:
                mx=ccc[i]
                mxe=i
            if ccc[i]==mx and i%2==0:
                if i<mxe:
                    mxe=i
        return mxe