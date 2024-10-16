n = input('Enter String : ')
length = len(n)

if length%2 != 0:
    print("String is not a pallindrom")
else:
    str1 = input[:length//2]
    str2 = input[length//2:]

    str1 = str2[::-1]

    if str1 == str2:
        print('string is a pallidnrom')
    else:
        print('not pallindrom')