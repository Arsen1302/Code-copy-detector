class Solution:
    def solution_1649_3_1(self, root, start: int) -> int:
        time_to_infect_tree, _ = self.solution_1649_3_2(root, start)
        return time_to_infect_tree

    def solution_1649_3_2(self, root, start):

        # if root is None
        if root == None:
            return -1, -1

        # get time to infect subtree from root, as well as distance from root of subtree
        # to the infected node (-1 if root is not a parent of it)
        left_infect_time, left_distance = self.solution_1649_3_2(root.left, start)
        right_infect_time, right_distance = self.solution_1649_3_2(root.right, start)

        # if both subtrees don't contain the infected node
        if left_distance == -1 and right_distance == -1:
            distance = -1
            # infect time is as if from root node, AKA simply the depth of the subtree
            infect_time = max(right_infect_time, left_infect_time) + 1

        # if left subtree contains the infected node
        elif left_distance != -1:
            # update distance to infected node
            distance = left_distance + 1
            # distance to the infected node from root.left, then two edges to root.right (+2), then
            # infect time of right subtree as if from root.right
            infect_time = max(left_infect_time, right_infect_time + left_distance + 2)
            
        # same as before, but with right subtree containing the infected
        else:
            distance = right_distance + 1
            infect_time = max(right_infect_time, left_infect_time + right_distance + 2)

        # if found the infected node
        if root.val == start:
            distance = 0

        return infect_time, distance