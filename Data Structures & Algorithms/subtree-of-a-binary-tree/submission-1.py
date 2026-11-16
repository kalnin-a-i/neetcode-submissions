class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def same_tree(a, b):
            if not a or not b:
                return a is b

            return (
                a.val == b.val
                and same_tree(a.left, b.left)
                and same_tree(a.right, b.right)
            )

        def search(node):
            if not node:
                return False

            return (
                same_tree(node, subRoot)
                or search(node.left)
                or search(node.right)
            )

        return subRoot is None or search(root)