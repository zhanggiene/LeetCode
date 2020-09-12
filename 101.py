# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def leftRight(left,right):
            if left.val==right.val:
                if left.left!=None and right.right!=None and left.right!=None and right.left!=None:
                    return leftRight(left.right,right.left) and leftRight(left.left,right.right)
                elif left.left!=None and right.right!=None and (left.right==None and right.left==None):
                    return leftRight(left.left,right.right)
                elif left.right!=None and right.left!=None and (left.left==None and right.right==None):
                    return leftRight(left.right,right.left)
                elif left.left==None and right.right==None and left.right==None and right.left==None:
                    return True
                else:
                    return False
            else:
                return False
        if root==None:
            return True
        elif root.left==None and root.right==None:
            return True
        elif root.left==None or root.right==None:
            return False
        return leftRight(root.left,root.right)