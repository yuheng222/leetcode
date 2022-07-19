class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        table = {}
        result = []
        # iterate through the numbers in the second array
        for num in nums2:
            # compare the current number with the previous number, if it is greater, add it to the hashmap
            while stack and num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            result.append(table.get(num, -1))
        return result
        