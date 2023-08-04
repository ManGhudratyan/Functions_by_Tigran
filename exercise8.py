# Գրել ֆունկցիա , որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված հակառակ։

def reverseString(mstr):
    tmp = "";
    for el in mstr:
        tmp = el + tmp;
    return tmp;
print(reverseString('hello world'));
