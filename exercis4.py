# Գրել ֆունկցիա , որը կստանա 2 արգումենտ և կվերադարձնի այդ արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։

def mathOperations(a, b):
    msum = a + b;
    sub = a - b;
    mult = a * b;
    
    if (b != 0):
        div = a // b;
    if (b > a):
        b,a = a,b;
        div = a // b;
    
    return {'Sum' : msum, 'Sub' : sub, 'Mult' : mult, 'Div' : div};
    
print(mathOperations(30, 15)); 

