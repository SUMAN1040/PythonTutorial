# def getSmaller(l, x):
#     res = []
#     for e in l:
#         if e < x:
#             res.append(e)
#     return res


# print("Print the list element: ")
# l = list(map(int, input().split()))
# x = 30
# print(getSmaller(l, x))


# def oddEven(n):
#     odd = []
#     even = []
#     for i in n:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return odd, even

# print("Print the list element:")
# n = list(map(int, input().split()))
# odd, even = oddEven(n)
# print(odd)
# print(even)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = [n for n in a if n % 2 == 0]
# odds = [n for n in a if n % 2 != 0]

# print(evens)  
# print(odds)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = list(filter(lambda n: n % 2 == 0, a))
# odds = list(filter(lambda n: n % 2 != 0, a))

# print(evens)  
# print(odds)



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = list(filter(lambda n: n % 2 == 0, a))
# odds = list(filter(lambda n: n % 2 != 0, a))

# print(evens)
# print(odds)

# evens, odds = [], []

# for n in a:
#     evens.append(n) if n % 2 == 0 else odds.append(n)

# print(evens)  
# print(odds)

# evens, odds, i = [], [], 0

# while i < len(a):
#     evens.append(a[i]) if a[i] % 2 == 0 else odds.append(a[i])
#     i += 1

# print(evens)
# print(odds)



# l1 = [x for x in range(11) if x % 2 == 0]
# print(l1)
# l2 = [x for x in range(11) if x % 2 != 0]
# print(l2)



def average(l):
    sum = 0
    for i in l:
        sum = sum + i
    n = len(l)
    return sum/n

l = [12, 23, 34]
print(average(l))