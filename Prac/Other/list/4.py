# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# avg = sum(a) / len(a)

# print(avg)




# a = [2, 4, 6, 8, 10]
# total = 0

# for val in a:
#     total += val

# avg = total / len(a)
# print(avg)




# import statistics

# a = [1, 2, 3, 4, 5]
# avg = statistics.mean(a)
# print(avg)



# import numpy

# a = [1, 2, 3, 4, 5]
# avg = numpy.average(a)

# print(int(avg))



# def cDistinct(l):
#     res = 1
#     for i in range(1, len(l)):
#         if l[i] not in l[0:i]:
#             res = res + 1
#     return res

# l = [10, 20, 30, 40, 50, 60]
# print(cDistinct(l))



# def distinct(l):
#     return len(set(l))

# l = [10, 20, 30, 40, 50, 60]
# print(distinct(l))





# def counting_distinct_elements(input_list):
#     return len(set(input_list))

# numbers = [10, 20, 30, 40, 50]
# print(counting_distinct_elements(numbers))


def sorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i - 1]:
            return False
        i = i + 1
    return True

l = [10, 20, 30, 40, 50]
if sorted(l):
    print("Yes")
else:
    print("No")





def isSort(l):
    s1 = sorted(l)
    if (s1 == l):
        return True
    else:
        return False
    
l = [10, 20, 5, 30]
if(isSort(l)):
    print("Yes")
else:
    print("No")



a = [1, 2, 3, 4, 5]

res = True

for i in range(len(a) - 1):
    if (a[i] > a[i  + 1]):
        res = False
        break

print(res)
