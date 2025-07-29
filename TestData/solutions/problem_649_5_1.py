class Solution:
    def solution_649_5_1(self, root: Optional[TreeNode]) -> int:
        hasCamera = False
        isMonitored = False
        return self.solution_649_5_2(root, hasCamera, isMonitored)

    # Hypothesis -> Will always return the minimum Cameras required
    def solution_649_5_2(self, root, hasCamera, isMonitored) -> int:
        # if no node, then no camera needed
        if root is None:
            return 0
        # ************************** BASE CASES *************************************************
        if hasCamera:
            # CASE - 1
            return 1 + self.solution_649_5_2(root=root.left, hasCamera=False, isMonitored=True) + self.solution_649_5_2(root=root.right, hasCamera=False, isMonitored=True)
        # no camera is present at node, which means node is monitored somehow
        if isMonitored:
            # CASE - 2
            # No camera at node, but child have camera, so we need cameras from left and right
            childWithCam = self.solution_649_5_2(root.left, hasCamera=False, isMonitored=False) + \
                self.solution_649_5_2(root.right, hasCamera=False, isMonitored=False)
            childWithNoCam = 1 + self.solution_649_5_2(root.left, hasCamera=False, isMonitored=True) + self.solution_649_5_2(
                root.right, hasCamera=False, isMonitored=True)
            # REMEMBER, THIS IS NOT THE FINAL ANSWER, IT IS JUST A BASE CASE
            return min(childWithCam, childWithNoCam)
        
        # REMEMBER, THIS IS TRICKY, 
        # DONT ADD, THIS BASE CASE FOR MEMOIZATION, BEFORE OTHER POSSIBLE BASE CASES
        # BECAUSE, THEY HAVE THEIR OWN RECURSIVE CALLS AND THEIR OWN OPERATIONS TO PERFORM
        if root.val != 0:
            return root.val
        # ************************************* INDUCTION ****************************************
        # Now, all the cases, when adding camera at out will
        # Try, adding camera at node or root
        rootHasCam = 1 + self.solution_649_5_2(root.left, hasCamera=False, isMonitored=True) + \
            self.solution_649_5_2(root.right, hasCamera=False, isMonitored=True)
        # Now, we have two cases, either add camera to left or right node
        leftHasCam = float("inf")
        if root.left is not None:
            leftHasCam = self.solution_649_5_2(root.left, hasCamera=True, isMonitored=False) + \
                self.solution_649_5_2(root.right, hasCamera=False, isMonitored=False)
        rightHasCam = float("inf")
        if root.right is not None:
            rightHasCam = self.solution_649_5_2(root.left, hasCamera=False, isMonitored=False) + \
                self.solution_649_5_2(root.right, hasCamera=True, isMonitored=False)
        # Now, we want minimum of all the cases
        # REMEMBER: - THIS MINIMUM IS THE FINAL ANSWER REQUIRED, SO MEMOIZE THIS
        root.val = min(rootHasCam, leftHasCam, rightHasCam)
        return root.val