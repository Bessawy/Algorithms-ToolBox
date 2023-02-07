def change(money):
    # write your code herE
    coins = [1, 3, 4]
    dp = [float('inf')] * (money + 1)
    dp[0] = 0.0

    for i in range(1, len(dp)):
        for c in coins:
            if(i - c < 0):
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return int(dp[-1])


if __name__ == '__main__':
    m = int(input())
    print(change(m))
