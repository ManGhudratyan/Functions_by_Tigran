# Գրել ֆունկցիա , որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված ամբողջությամբ մեծատառ (upper ֆունկցիան օգտագործել չի կարելի ) ։

def isUpper(mstr):
    if type(mstr) != str:
        print('Write only string!');
        return None;
    upperWord = "";
    for el in mstr:
        if (ord(el) >= 97 and ord(el) <= 122):
            el = chr(ord(el) - 32);
        upperWord += el;
    return upperWord;

print(isUpper('hello world!'));
