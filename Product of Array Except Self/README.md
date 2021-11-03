# Problem Description
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  ```[1, 7, 3, 4]```

Python 3.6
your function would return:

 ``` [84, 12, 28, 21]```

Python 3.6
by calculating:

  ```[7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]```

Python 3.6
Here's the catch: You can't use division in your solution!

## Problem solution
### Description:
The solution can be broken down into smaller steps. For each number, we are multiplying the product of the numbers before it by the multiplication of those after it. By calculating these values, we can pass through the array only twice to arrive at the solution.
### Complexity: 
O(n). We only iterate through the array twice
