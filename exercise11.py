# Գրել ֆունկցիա , որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։

def mostUsedLetter(mstr):
    maxLetter = "";
    count = 0;
    for el in mstr:
        if (mstr.count(el) > count):
            count = mstr.count(el);
            maxLetter = el;
    return maxLetter, count;
    
mstr = mostUsedLetter('hello world');
print('Most used letter is', mstr);

