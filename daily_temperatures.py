# Time complexity - O(n)
# Space complexity - O(n) # the stack

# Approach - Maintain a monotonic stack, traverse the array and pop the elements from stack only if the top
# element of stack is less than the current temperature.

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        result = [0 for i in range(n)]

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                popped = st.pop()
                result[popped] = i - popped
            st.append(i)
        return result