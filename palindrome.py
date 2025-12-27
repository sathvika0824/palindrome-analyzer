class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        if x < 0:
            return False
        else:
            reverse = str(x)[::-1]
            rev = int(reverse)
            if original == rev:
                return True
            else:
                return False
