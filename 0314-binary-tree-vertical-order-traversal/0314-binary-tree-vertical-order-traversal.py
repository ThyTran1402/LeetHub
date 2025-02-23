# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashTable = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            if node is not None:
                hashTable[col].append(node.val)
                
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
                
        return [hashTable[i] for i in sorted (hashTable.keys())]
    
#BFS traversal
#Time complexity: O(Nlog N)-> N is the number of nodes in the tree
#Space complexity: O(N)