class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''

        ans = str(t.val)
        if t.left or t.right:
            ans += '(' + self.tree2str(t.left) + ')'
        if t.right:
            ans += '(' + self.tree2str(t.right) + ')'
        return ans






        """
        You need to construct a string consists of parenthesis and integers from a binary tree with the
        preorder traversing way.

        The null node needs to be represented by empty parenthesis pair "()". And you need to omit all
        the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the
        string and the original binary tree.

        Example 1:

        Input: Binary tree: [1,2,3,4]
           1
         /   \
        2     3
        /
        4

        Output: "1(2(4))(3)"

        Explanation: Originallay it needs to be "1(2(4)())(3()())",
        but you need to omit all the unnecessary empty parenthesis pairs.
        And it will be "1(2(4))(3)".

        """
