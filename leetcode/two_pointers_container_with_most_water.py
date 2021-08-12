from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # dp = (min(height), len(height))
        max_square = min(height[0], height[-1]) * (len(height) - 1)
        begin = 0
        end = len(height)
        # max_square = 0
        while begin < end - 1:
            if height[begin] <= height[end - 1]:
                begin += 1
            else:
                end -= 1
            current_square1 = min(height[begin], height[end - 1]) * (end - begin - 1)
            print(f'{height[begin:end]}: {current_square1}')
            # end -=1
            # current_square2 = min(height[begin], height[end - 1]) * (end - begin - 1)
            # print(f'{height[begin:end]}: {current_square2}')
            max_square = max(current_square1, max_square)
            
        return max_square

if __name__ == '__main__':
    s = Solution()
    # s.maxArea([1,8,6,2,5,4,8,3,7])
    # s.maxArea([1,2,1])  # 2
    # s.maxArea([1,1])
    # s.maxArea([2,3,4,5,18,17,6])  # 17
    s.maxArea([2, 1])  # 17