class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(sub):
            rev = sub[::-1]
            if sub == rev:
                return True
            return False
        counter = 0
        for i in range(len(s)):
            #print('i:',i)
            for j in range(i, len(s)):
                #print('j:', j)
                #print(s[i: j+1])
                if is_palindrome(s[i: j+1]):
                    counter = counter + 1
        return counter
