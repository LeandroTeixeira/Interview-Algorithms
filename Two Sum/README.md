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

# Problem solution
## Description:
The solution can be broken down into smaller steps. For each number, we are multiplying the product of the numbers before it by the multiplication of those after it. By calculating these values, we can pass through the array only twice to arrive at the solution.
## Complexity: 
O(n). We only iterate through the array twice
