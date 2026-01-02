class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            False

        org_x = x
        rev_x = 0

        while x > 0:
            rem = x % 10
            rev_x = (rev_x * 10) + rem
            x //= 10

        return rev_x == org_x