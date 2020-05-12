#This software checks if a word is a palindrome or not.

def palindrome(str):
    str = str.casefold().replace(" ","",-1).replace("'","",-1)
    stringlength=len(str)
    slicedString=str[stringlength::-1]
    if str == slicedString:
        print("True")
    else:
        print("False")

to_analyze = input(str("Is it a palindrome? "))
palindrome(to_analyze)