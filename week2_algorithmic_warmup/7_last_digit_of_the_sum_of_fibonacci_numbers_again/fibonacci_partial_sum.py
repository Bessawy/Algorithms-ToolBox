# Uses python3
import sys

def fibonacci_partial_sum_naive2(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def fibonacci_partial_sum_naive(from_, to):
    f = fibPeriod(10)
    p = len(f)
    last_index = to % p
    first_index = from_ %p
    noOfperiods = int(to/p)
    sumOfperiod = sum(f)
    sumOflast = sum(f[:last_index+1])
    sumOfAllTolast = noOfperiods * sumOfperiod + sumOflast
    return (sumOfAllTolast - sum(f[:first_index]))%10



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
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
    #print(fibonacci_partial_sum_naive2(from_, to))

