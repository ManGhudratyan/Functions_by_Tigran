# Գրել ֆունկցիա , որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված ամբողջությամբ փոքրատառ (lower ֆունկցիան օգտագործել չիկարելի ) ։

def isLower(mstr):
    if type(mstr) != str:
        print('Write only string!');
        return None;
    lowerWord = "";
    for el in mstr:
        if (ord(el) >= 65 and ord(el) <= 90):
            el = chr(ord(el) + 32);
        lowerWord += el;
    return lowerWord;

print(isLower('Hello WORLD!'));
