# Time complexity - O(2n) # need to traverse array twice
# Space complexity - O(n) # the stack

# Approach - Maintain a monotonic stack, traverse the array twice because we need to go circular, append
# stack only if i < n (only the first traversal).

from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if nums == None or len(nums) == 0:
            return []
        st = []
        n = len(nums)
        result = [-1 for i in range(n)]

        for i in range(2*n):
            while st and nums[i % n] > nums[st[-1]]:
                popped = st.pop()
                result[popped] = nums[i % n]
            if i < n:
                st.append(i)
        
        return result