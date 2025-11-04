class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer array with 0s.
        stack = []  # This will store indices of the temperatures in decreasing order.

        # Traverse the array from right to left.
        for i in range(n - 1, -1, -1):
            # While the stack is not empty and the current temperature is greater
            # than or equal to the temperature at the index stored in the stack, pop the stack.
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            # If the stack is not empty, the top element of the stack will represent
            # the index of the next warmer day.
            if stack:
                answer[i] = stack[-1] - i
            
            # Push the current day index onto the stack.
            stack.append(i)

        return answer
        
