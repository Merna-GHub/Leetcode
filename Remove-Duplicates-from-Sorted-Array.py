1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        uniq_pos = 0
4        prev = 0
5        
6        for i in range(len(nums)):
7            if nums[uniq_pos] < nums[i]:
8                uniq_pos+=1
9                nums[uniq_pos] = nums[i]
10                
11        return uniq_pos+1
12            
13        