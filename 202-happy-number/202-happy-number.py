class Solution:
    def isHappy(self, n: int) -> bool:
        def find_square_sum(num):
            digit_sum = 0
            while num > 0:
                digit = num % 10
                digit_sum += digit * digit
                num //= 10
            return digit_sum
        
        slow, fast = n, n
        while True:
            slow = find_square_sum(slow)
            fast = find_square_sum(find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1
        