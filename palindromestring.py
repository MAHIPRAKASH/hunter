m=int(input("enter the length:\n"))
def is_palindrome(m):
    if len(m) < 1:
        return True
    else:
        if m[0] == m[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
     print("String isn't a palindrome!")
