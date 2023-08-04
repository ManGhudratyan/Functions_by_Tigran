# Գրել ֆունկցիա , որը կվերդարձնի ստացած արգումենտներից թվերի գումարը

def sum_numbers(*args):
    msum = 0;
    for num in args:
        msum += num;
    return msum;
    
numbers = sum_numbers(10, 25, 35, 45);
print('Sum of the numbers are', numbers);