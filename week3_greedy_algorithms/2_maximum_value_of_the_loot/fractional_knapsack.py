from sys import stdin

def optimal_value(capacity, weights, values):
    values = [values[i]/weights[i] for i in range(len(values))]
    total = 0
    values_sorted = sorted(list(enumerate(values)), key=lambda x: x[1], reverse=True)
    for index, val in values_sorted:        
        if(weights[index] <= capacity):
            total += val * weights[index] 
        else:
            total += val * capacity
            return total
        capacity -= weights[index]
        
    return total

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

    
