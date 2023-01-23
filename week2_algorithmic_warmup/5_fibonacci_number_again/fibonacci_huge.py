def fibonacci_huge_naive(n, m):
    f = febseq(m)
    p= len(f)
    return f[n%p]

def febseq(m):
    f = []
    f.append(0)
    f.append(1)

    i = 2
    while(1):
        next = (f[i - 1] + f[i - 2])%m
        f.append(next)

        i+=1

        if(f[-1] == 1 and f[-2] == 0):
            return f[0:-2]



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))


