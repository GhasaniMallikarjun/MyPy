def commonLetters():
    str1=input("Enter Your First String: ")
    str2=input("Enter your Second String: ")

    s1=set(str1)
    s2=set(str2)

    lst=s1 & s2

    print(lst)


commonLetters()