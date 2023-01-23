def fibonacci_sum_squares2(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    f = fibPeriod(10)
    f2 = [i*i for i in f]
    p = len(f)
    index = n % p
    noOfperiods = int(n/p)
    sumOfperiods = sum(f2) * noOfperiods
    return (sumOfperiods + sum(f2[:index+1]))%10


def fibPeriod(m):
    f = []
    f.append(0)
    f.append(1)

    i = 2
    while(1):
        next = (f[i - 1] + f[i - 2])%m
        f.append(next)
        i+=1
        
        if(f[i-1] == 1 and f[i - 2] == 0):
            return f[:-2]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
    #print(fibonacci_sum_squares2(n))
