#Using String slicing
# s = "GeeksForGeeks"
# rev = s[::-1]
# print(rev)


#Using reversed() and join()
# s = "SumanKumarDey"
# rev = ''.join(reversed(s))
# print(rev)



#Using Loop
# s = "SumanKumarDey"

# rev = ""

# for ch in s:
#     rev = ch + rev

# print(rev)




#Using the list comprehension and join()
# s = "Suman"
# rev = ''.join(s[i] for i in range(len(s) - 1, -1, -1))
# print(rev)


#Using Stack
s = "Suman"
stack = list(s)
rev = ""
while stack:
    rev += stack.pop()
print(rev)