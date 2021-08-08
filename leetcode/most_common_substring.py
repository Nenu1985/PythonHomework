

def main(s1: str, s2: str) -> str:
    
    
    dp = [[0] * len(s2) for _ in range(len(s1))]
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(s1[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[i][j]

if __name__ == '__main__':
    print(main('7123456543453', '7023345665438'))