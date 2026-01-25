1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        fact = int(len(nums)/2)
4        ans=[]
5
6        for x in range(fact):
7            ans.append(nums[x])
8            ans.append(nums[x+fact])
9
10        return ans