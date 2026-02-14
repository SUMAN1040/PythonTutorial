# s = input()
# i, j = 0, len(s) - 1
# is_palindrome = True

# while i < j:
#     if s[i] != s[j]:
#         is_palindrome = False
#         break
#     i += 1
#     j -= 1

# if is_palindrome:
#     print("Yes")
# else:
#     print("No")




#Using all() with Generator Expression
# s = "SumuS"

# if all(s[i] == s[-i-1] for i in range(len(s) // 2)):
#     print("Yes")
# else:
#     print('No')


#Using Slicing
# s = "malayalam" 

# if s == s[::-1]:
#     print("Yes")
# else:
#     print("No")

#Using Reverse Join
# s = "geeks"
# rev = ''.join(reversed(s))

# if s == rev:
#     print("Yes")
# else:
#     print("No")


