class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        res = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                res+=i
        return True if res == res[::-1] else False
        
