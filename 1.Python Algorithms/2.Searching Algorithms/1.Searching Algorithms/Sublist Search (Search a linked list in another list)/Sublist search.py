def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = "LIST NOT FOUND"

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = "LIST FOUND"

    return sub_set


a = [2, 4, 3, 5, 7]
b = [4, 3]
print(is_Sublist(a, b))