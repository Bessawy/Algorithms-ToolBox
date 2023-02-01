def change(money):
    # write your code here
    coins = [1, 5, 10]
    count = 0
    Minamount = money - coins[0]
    amount = coins[0]
    
    while(money):
        for c in coins:
            if(money - c >= 0 and money - c < Minamount):
                amount = c
        money-= amount
        count+=1 

    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
