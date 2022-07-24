class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_product = 0
        for num in nums:
            xor_product ^= num
        bitmask = 1
        # get the rightmost bit that is 1
        while bitmask & xor_product == 0:
            bitmask = bitmask << 1
        num1, num2 = 0, 0
        for num in nums:
            if num & bitmask != 0: # if bit is set
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]