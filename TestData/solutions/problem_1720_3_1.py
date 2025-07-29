class Solution:
    def solution_1720_3_1(self,nums):
        dict2 = {n:j for j,n in enumerate(sorted(nums))}

        count, i = 0, 0

        while i < len(nums):
            j = dict2[nums[i]]

            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
            else:
                i += 1

        return count

    def solution_1720_3_2(self, root):
        if not root:
            return 0

        dict1 = defaultdict(list)

        def solution_1720_3_3(node,level):
            if not node:
                return 0

            dict1[level].append(node.val)

            solution_1720_3_3(node.left,level+1)
            solution_1720_3_3(node.right,level+1)

        solution_1720_3_3(root,0)

        ans = list(dict1.values())

        return sum([self.solution_1720_3_1(i) for i in ans])