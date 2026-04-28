# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : 
            return []
        
        output = []
        if root : 
            output.append(root.val)

            if root.left : 
                output.extend(self.preorderTraversal(root.left))
            
            if root.right : 
                output.extend(self.preorderTraversal(root.right))

        return output
