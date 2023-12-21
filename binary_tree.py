class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Populating a height-balanced binary search tree recursively, assuming sorted array
class Solution(object):
    def array_to_BST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.array_to_BST(nums[:mid])
        root.right = self.array_to_BST(nums[mid + 1:])

        return root

    print(array_to_BST(sample))

# Finding minimum depth recursively

def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None: return 0   # return depth as 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1

        # If left tree is empty, return depth of right subtree after adding 1
        if root.left is None:
            return 1 + rightDepth
        # If right tree is empty, return depth of left subtree after adding 1
        if root.right is None:
            return 1 + leftDepth

        # Pick minimum of depths when two child functions return them and add 1
        return min(leftDepth, rightDepth) + 1
        # The extra +1 is the current node which is the parent of the two subtrees.
