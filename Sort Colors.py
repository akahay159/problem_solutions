'''
https://leetcode.com/problems/sort-colors/

'''

class Solution:
    def sortColors(self, a: List[int]) -> None:
        white, red = 0,0
        for i in range(len(a)):
            color = a[i]
            a[i] = 2
            
            if color < 2:
                a[white] = 1
                white += 1
            if color == 0:
                a[red] = 0
                red += 1