def optimal_summands(n):
    summands = []
    # write your code here
    total = 0
    val = 0

    while(True):

        val+=1  #2
        total+=val #3

        if(total > n):
            summands.pop() #0  
            total -= (2*val - 1) #3 - 2*2 + 1 = 0
            val-= 1
        elif(total == n):
            summands.append(val)
            break
        else:
            summands.append(val)    

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)