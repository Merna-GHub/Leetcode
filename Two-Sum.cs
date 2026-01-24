1public class Solution {
2    public int[] TwoSum(int[] nums, int target) {
3        Dictionary<int,int> map = new Dictionary<int,int>();
4        
5        for(var i = 0 ; i < nums.Length ; i++){
6            var diff = target - nums[i];
7            if(map.ContainsKey(diff)){
8                return new int[]{i, map[diff] };
9            }
10
11            if(!map.ContainsKey(nums[i])){
12                map.Add(nums[i], i);
13            }
14        }
15        return new int[0];
16    }
17}