def lcs3(first_sequence, second_sequence, third_sequence):
    m, n, k = len(first_sequence), len(second_sequence), len(third_sequence)
    T = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]

    for v in range(1, k + 1):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if(first_sequence[i-1] == second_sequence[j-1] == third_sequence[v - 1]):
                    T[v][i][j] = T[v-1][i-1][j-1] + 1
                else:
                    T[v][i][j] = max(T[v][i-1][j], T[v][i][j-1], T[v-1][i][j], 
                        T[v][i-1][j-1], T[v-1][i][j-1], T[v-1][i-1][j]
                        )

    return T[k][m][n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
