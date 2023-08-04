# Գրել ֆունկցիա , որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։

def countStr(*args):
    count = 0;
    for el in args:
        if (type(el) == str):
            count += 1;
    return count;
stringCount = countStr("Hello", 45, "Good", [10, 40, 90], "World!", 65);
print("Number of strings:", stringCount);

