'''
Code problems: covering segments by points

Given n segments, find the minimal possible number of points such that each segment contains at least one point.

The first line contains the number 1≤n≤100 of segments. Each of the following n lines contains two integers 0≤l≤r≤109 defining the endpoints of a segment. Output the optimal number m of points and then m points. 

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3 

Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 

Memory Limit: 256 MB
Time Limit: 1 seconds
'''

# listOfTuples = []
# n = int(input())
# for i in range(n):
#     beg, end = map(int, input().split())
#     listOfTuples.append((beg, end))

def main(listOfTuples):
    sortedBeg = sorted(listOfTuples, key=lambda x: x[0])
    sortedEnd = sorted(listOfTuples, key=lambda x: x[1])

    thrhold = sortedBeg[0][0] - 1
    listOfPoints = []
    for i in range(len(sortedEnd)  -1):
        beg, end = sortedEnd[i]
        if beg > thrhold:
            listOfPoints.append(end)
            thrhold = end

    last_point = listOfPoints[len(listOfPoints) - 1]
    beg_of_last_sorted_end = sortedEnd[len(sortedEnd) - 1][0]
    if last_point < beg_of_last_sorted_end:
        if sortedEnd:
            listOfPoints.append(beg_of_last_sorted_end)
    print(len(listOfPoints))
    result = []
    for p in listOfPoints:
        result.append(p)

    print(*result)

if __name__ == '__main__':
    # main([[4, 7], [1, 3], [2, 5], [5 ,6]])
    # main([[1,2], [3,4]])
    main([[-1,3], [-5,-3], [3,5], [2,4], [-3,-2], [-1, 4], [5,7]])