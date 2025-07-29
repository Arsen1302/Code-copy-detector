class Solution:
    def solution_1695_2(self, nums: List[int]) -> int:
        n=len(nums)
		#traversing through loop
        for i in range(n):
            nums.append(int(str(nums[i])[::-1])) #using string slicing and appending reverse of the number at end
        return len(set(nums)) #returning the length of set to get unique value count