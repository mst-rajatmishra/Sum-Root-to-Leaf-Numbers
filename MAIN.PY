# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current path sum
            current_sum = current_sum * 10 + node.val
            
            # If we reach a leaf node, return the current path sum
            if not node.left and not node.right:
                return current_sum
            
            # Continue DFS on left and right children
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        # Start DFS from the root with initial sum of 0
        return dfs(root, 0)

# Example usage
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.sumNumbers(root1))  # Output: 25

root2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(solution.sumNumbers(root2))  # Output: 1026
