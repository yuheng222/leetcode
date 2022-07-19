class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        table = {}
        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)
            
        return [table.get(num, -1) for num in nums1]
        