def compute_operations(n):
    arr = [0] * (n + 1)
    arr[1] = 0
    
    for i in range(2, n+1):
        op = [float("inf")] * 3
        if(i%2==0):
            op[1] = 1 + arr[i//2]
        if(i%3==0):
            op[0] = 1 + arr[i//3]
        op[2] = 1 + arr[i-1]
        arr[i] = min(op)

    output = [n]  
    j = n  
    while(j > 1):
        op = []
        if(j%2==0):
            op.append(j//2)
        if(j%3==0):
            op.append(j//3)

        op.append(j-1)
        minValue = min([(arr[x], x) for x in op])
        output.append(minValue[1])
        j = minValue[1]

    return list(reversed(output))


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
