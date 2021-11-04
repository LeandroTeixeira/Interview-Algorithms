# Problem Description  _[(source)](https://leetcode.com/problems/two-sum/)_
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Problem solution
### Description:
The idea is pretty simple: We iterate once on the array. For each number, we calculate which number we need to add up to the target and checks if the number exists in a hash map. If it doesn't, we save the current number in that hash map alongside it's position. Using this, we only need to iterate the array once and since hash maps go for O(1) on average, the time complexity is kept at O (n).

### Complexity: 
O(n). We only iterate through the array once and hash maps have O (1) on average.
