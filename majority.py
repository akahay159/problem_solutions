

https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1, count1 = None, 0
        element2, count2 = None, 0
        for i in nums:
            if(i == element1):
                count1 += 1
            elif(i == element2):
                count2 += 1
            elif(count1 == 0):
                element1 = i
                count1 = 1
            elif(count2 == 0):
                element2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        #ans = [n for n in (element1, element2) if(nums.count(n)) > len(nums)//3]
        answer = []
        count1, count2 = 0, 0
        k = len(nums) // 3
        for i in nums:
            if i == element1:
                count1 += 1
            if i == element2:
                count2 += 1
        if count1 > k:
            answer.append(element1)
        if count2 > k:
            answer.append(element2)
        return answer
        
        