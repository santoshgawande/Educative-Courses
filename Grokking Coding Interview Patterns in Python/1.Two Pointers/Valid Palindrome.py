#
# Example : madam
#
def is_palindrome(s):
  
  # Replace this placeholder return statement with your code
  left = 0
  right = len(s) - 1
  while left <= right:
    if s[left] != s[right]:
      return False
    left = left + 1
    right = right-1 

  return True

# res = is_palindrome("madam")
# print("res :", res)