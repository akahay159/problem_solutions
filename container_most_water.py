'''https://leetcode.com/problems/container-with-most-water/ '''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, left, right = 0, 0, len(height)-1
        while left < right :
            area = max(area,min(height[left], height[right]) * (right - left))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return area



// Time complexity: O(n)
// Space complexity: O(1)
        