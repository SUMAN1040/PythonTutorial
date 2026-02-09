# Basic String Operation
# def access_char_by_index(s, k):
#     return s[k]

# if __name__ == "__main__":
#     s = "SumanKumarDey"
#     k = 4
#     print(access_char_by_index(s, k))




# Inserting Character/String into an String
# def insert_demo(s, ch, k):
#     modified_string = s[:k] + ch + s[k:]
#     print("Modified String: ", modified_string)

# if __name__ == "__main__":
#     s = "GeeksGeeks"
#     ch_to_insert = "for"
#     index_to_invert = 5

#     print("Original String: ", s)
#     insert_demo(s, ch_to_insert, index_to_invert)


#Modifying Character in string
# def replace_ch(s, index, ch):
#     lst = list(s)

#     lst[index] = ch

#     return ''.join(lst)

# if __name__ == "__main__":
#     s = "Geeks Gor Geeks"
#     index = 6
#     ch = 'F'

#     print("Original String =", s)
#     s = replace_ch(s, index, ch)
#     print("Modified String =", s)



#Deletion of character in String
# def remove(s, c):
#     return ''.join([ch for ch in s if ch != c])

# if __name__== "__main__":
#     s = "GeeksForGeeks"
#     s = remove(s, 'g')
#     print(s)



#Concatenating String(combining multiple string into one)
# def main():
#     init = "this is init"
#     add = " added now"

#     result = init + add

#     print(result)

# if __name__ == "__main__":
#     main()




#Finding the length/size of a string
# def main():
#     str = "GeeksForGeeks"
#     print(len(str))

# if __name__ == "__main__":
#     main()



#Comparing String for Equality
def compare_string(s1, s2):
    if s1 != s2:
        print("S1 not equal to s2")
        if s1 > s2:
            print("S1 is greater than s2")
        else:
            print("S2 is greater than s1")
    else:
        print("S1 is equal to s2")

compare_string("Geeks", "forGeeks")
compare_string("Geeks", "geeks")