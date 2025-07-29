class Solution:
    def solution_668_4_1(self):
        pass

    def solution_668_4_2(self, root) -> str:
        self.rlex = ""
        self.solution_668_4_3(root)
        return self.rlex

    def solution_668_4_3(self, root, lex=""):
        if root.left:
            self.solution_668_4_3(root.left, chr(root.val + 97) + lex)
        if root.right:
            self.solution_668_4_3(root.right, chr(root.val + 97) + lex)
        if root.left is None and root.right is None and self.rlex != "":
            self.solution_668_4_4(chr(root.val + 97) + lex, self.rlex)
            return
        elif root.left is None and root.right is None:
            self.rlex = chr(root.val + 97) + lex

    def solution_668_4_4(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        i = 0
        if n1 < n2:
            while i < n1:
                if s1[i] < s2[i]:
                    self.rlex = s1
                    return
                elif s2[i] < s1[i]:
                    self.rlex = s2
                    return

                i += 1
            self.rlex = s1
        else:
            while i < n2:
                if s1[i] < s2[i]:
                    self.rlex = s1
                    return
                elif s2[i] < s1[i]:
                    self.rlex = s2
                    return

                i += 1
            self.rlex = s2