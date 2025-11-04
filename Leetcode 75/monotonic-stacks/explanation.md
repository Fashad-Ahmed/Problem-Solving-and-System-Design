### Problem Statement:

Given an array temperatures where temperatures[i] is the temperature of the day i, return an array answer where answer[i] is the number of days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Solution Using Monotonic Stack:

A monotonic stack is a stack that maintains elements in a certain order (either strictly increasing or strictly decreasing). To solve this problem, we can use a monotonic decreasing stack.

 ### Key Idea:

We will traverse the temperatures array from right to left.

Use a stack to store the indices of the temperatures, ensuring that the temperatures in the stack are in decreasing order.

For each temperature at index i, check the stack to find the next warmer temperature (i.e., find the nearest future day with a temperature greater than the current one).

If the stack is empty, there’s no future warmer day, so set the answer for that day as 0.

If the stack is not empty, the top of the stack will represent the index of the next warmer day. The difference between the current index and that index gives the number of days you need to wait for a warmer day.

### Algorithm:

Traverse the array from right to left.

For each day, pop elements from the stack that represent temperatures less than or equal to the current temperature.

If the stack is not empty after popping, the top of the stack will give the next warmer day.

Push the current day’s index onto the stack.

### Explanation of Code:

answer = [0] * n: Initialize the result array with all zeros, which will hold the number of days to wait for a warmer temperature.

stack = []: We use a stack to store the indices of the temperatures, ensuring the temperatures are in decreasing order in the stack.

Looping through temperatures from right to left: Start from the last element and go backward. For each temperature:

Pop elements from the stack that represent temperatures less than or equal to the current temperature because we want to find the next warmer day.

If there are still elements in the stack, the top element represents the index of the next warmer day. The number of days to wait is the difference between this index and the current index.

Push the current index onto the stack after processing.

Return the answer array, which now contains the number of days to wait for a warmer temperature for each day.




### Example Walkthrough:

For the input:

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


Start from the last day (index 7) where the temperature is 73. There is no warmer day ahead, so answer[7] = 0.

Move to index 6 (temperature 76). There is no warmer day ahead, so answer[6] = 0.

Move to index 5 (temperature 72). The next warmer day is at index 6 (temperature 76), so answer[5] = 1 (6 - 5).

Continue this process for each index.

Final output:

[1, 1, 4, 2, 1, 1, 0, 0]



### Time and Space Complexity:

Time Complexity: O(n), where n is the length of the input array. Each element is pushed and popped from the stack at most once.

Space Complexity: O(n), where n is the length of the input array. We use an additional stack to store the indices.

### What is a Monotonic Stack? 

A monotonic stack is a stack that maintains its elements in a specific order: either monotonically increasing or monotonically decreasing.

Monotonically increasing stack: The stack’s elements are ordered in increasing order, i.e., each new element must be greater than or equal to the previous one.

Monotonically decreasing stack: The stack’s elements are ordered in decreasing order, i.e., each new element must be less than or equal to the previous one.

