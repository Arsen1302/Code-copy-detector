class Solution:
    def solution_136_5(self, citations: List[int]) -> int:
        start=0
        n=len(citations)
        end=len(citations)-1
        while start<=end:
            mid=start+(end-start)//2
            if citations[mid]==(n-mid):
                return citations[mid]
            elif citations[mid]>(n-mid):
                end=mid-1
            else:
                start=mid+1
        return (n-start)