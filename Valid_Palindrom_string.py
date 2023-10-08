class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t=s.lower()
        z = ''.join(c for c in t if c.isalnum())
        if z==z[::-1]:
            return True
        else:
            return False
        
        