def maxWeight(capacity, items):
    n = len(items)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            T[i][w] = T[i - 1][w]
            if(w - items[i - 1] >= 0 ):
                T[i][w] = max(T[i - 1][w - items[i - 1]] + items[i - 1], T[i][w])
    
    return T[n][capacity]


def otimalSolution(T, capacity, items):
    i = len(items)
    w = capacity
    optimal = []

    while(i>0 and w>0):
        if T[i][w] == T[i-1][w]:
            i -= i
        else:
            optimal.append(items[i - 1])  
            i-=1
            w-=items[i-1]  
    return optimal


ipt = input()
W, n = map(int, ipt.split())
ipt = input()
weights = list(map(int, ipt.split()))
print(maxWeight(W, weights))