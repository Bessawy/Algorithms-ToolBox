def fibonacci_sum2(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum(n):
    f = fibPeriod(10)
    p = len(f)
    sumOfSingleP = sum(f)
    nOfPeriodsExceptLast = int(n / p)
    index = n % p 
    sumOfLastP = sum(f[:index+1])
    return (sumOfSingleP * nOfPeriodsExceptLast + sumOfLastP)%10

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
    print(fibonacci_sum(n))

