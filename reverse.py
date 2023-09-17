def reverse_st(st):
    str = " "
    for i in st :
        str = i + str
    return str   

st = "savyasanchi"
print(st)
print("The reverse string is " , reverse_st(st))
