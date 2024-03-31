

def lev_recursivo(a, b):
    def cabeca(a):
        return a[0]

    def cauda(a):
        return a[1:]
    
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if cabeca(a) == cabeca(b):
        return lev_recursivo(cauda(a), cauda(b))
    return 1 + min(
        lev_recursivo(cauda(a), b),
        lev_recursivo(a, cauda(b)),
        lev_recursivo(cauda(a), cauda(b))
    )


def lev_iterativo(a, b):
    d = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        d[i][0] = i
    for j in range(len(b) + 1):
        d[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
            )
    return d[len(a)][len(b)]


if __name__ == '__main__':
    print(f'lev_iterativo: {lev_iterativo("paulo", "pedro")}')
    print(f'lev_recursivo: {lev_recursivo("paulo", "pedro")}')
    print(lev_iterativo('Quantos anos tem o Python?', 'quantos Python tem os anos?'))
    print(lev_recursivo('Quantos anos tem o Python?', 'quantos Python tem os anos?'))