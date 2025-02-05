"""
class tree node
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """
    Given the root of a binary tree, check whether it is a mirror of itself 
    (i.e., symmetric around its center).
    Input: root = [1,2,2,3,4,4,3]
    Output: true
    """
    def isSymmetric(self, root):
        def isSame(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return(left.val == right.val and \
                   isSame(left.left, right.right) and \
                    isSame(left.right, right.left))
        return isSame(root.left, root.right)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

solution = Solution()
result = solution.isSymmetric(root)
print(result)