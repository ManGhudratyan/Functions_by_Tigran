# Գրել ֆունկցիա , որը կվերադարձնի նախադասության ամենաերկար բառը։

def longWord(mstr):
    splited = mstr.split();
    longWord = "";
    for el in splited:
        if len(el) > len(longWord):
            longWord = el;
    return longWord;
print(longWord('Hello good and beautiful world!'))
