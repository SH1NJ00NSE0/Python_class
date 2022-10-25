def palindrome(string):
   return list(string)==list(reversed(string))

string = input()
print(palindrome(string))
