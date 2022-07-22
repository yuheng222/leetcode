class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num):
            digit_sum = 0
            while num > 0:
                digit = num % 10
                digit_sum += digit * digit
                num //= 10
            return digit_sum
        slow, fast = n, n
        while True:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))
            if slow == fast:
                break
        return slow == 1
            
        