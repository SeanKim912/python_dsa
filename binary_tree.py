class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Populating a height-balanced binary search tree recursively, assuming sorted array

def array_to_BST(self, nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = self.array_to_BST(nums[:mid])
    root.right = self.array_to_BST(nums[mid + 1:])

    return root

print(array_to_BST(sample))
