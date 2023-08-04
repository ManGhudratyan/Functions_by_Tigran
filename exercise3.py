# Գրել ֆունկցիա , որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։

def findAvg(*args):
    msum = 0;
    for i in args:
        msum += i;
    avg = msum / len(args);
    return avg;

print(findAvg(10, 20, 30, 40, 50));

# other version
def findAvg(*args):
    return sum(args) / len(args);
    
print(findAvg(10, 20, 30, 40, 50));