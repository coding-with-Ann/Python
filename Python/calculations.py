y = 6

def add(a,b):
    result = a+b
    return result

def multi(a,b):
    return a*b
def div(a,b):
    return a/b


def checkAnagram(s1,s2):
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")