
def levenstein(s1: str, s2: str):
    
    # F00 = 0; Fio = i; F0j = j;
    '''
    F = 
    0:[0, 1, 2, 3, 4, 5, 6]
    1:[1, 0, 0, 0, 0, 0, 0]
    2:[2, 0, 0, 0, 0, 0, 0]
    3:[3, 0, 0, 0, 0, 0, 0]
    4:[4, 0, 0, 0, 0, 0, 0]
    5:[5, 0, 0, 0, 0, 0, 0]
    '''
    F = [[(i + j) if i * j == 0 else 0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[i][j]


if __name__ == '__main__':
    print(levenstein('sugar', 'kufar1'))