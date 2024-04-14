# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, node):
        queue = [node]
        ans = 0
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left is not None:
                if current_node.left.left is None and current_node.left.right is None:
                    ans += current_node.left.val
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return ans
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)


