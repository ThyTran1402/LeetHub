class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 ^ i for i in reversed(row)] for row in image]
    
    
# Time complexity: O(N)
# Space complexity: O(1)