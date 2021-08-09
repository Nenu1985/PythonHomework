from typing import List


def back_pack(weights: List[int], prices: List[int], max_weight: int) -> int:
    
    dp = [[0] * (max_weight + 1) for _ in range(len(weights) + 1)]
    # i - num of item ot pick up into backpack
    # j - stands for alowable weight
    for i in range(1, len(weights) + 1):
        for j in range(max_weight + 1):
            if j - weights[i-1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i-1]] + prices[i - 1])
    return dp[i][j]


if __name__ == '__main__':
    print(back_pack([6,4,3,2,5], [5,3,1,3,6], 15))
