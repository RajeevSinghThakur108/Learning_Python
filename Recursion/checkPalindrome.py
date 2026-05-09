def checkPalindrome(s,left , right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return checkPalindrome(s,left+1 , right-1)
s="madkam"
print(checkPalindrome( s, 0, len(s)-1 ) , " palindrome")
    