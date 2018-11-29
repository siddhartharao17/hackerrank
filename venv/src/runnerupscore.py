def runnerUpScore(arr):
    scoreFirst, scoreSecond = 0,0
    arr = sorted(arr)
    # print(type(arr))
    maxIndex = len(arr) - 1
    for i in range(maxIndex, -1, -1): # loops backwards
        # print(i)
        if arr[i] != arr[i-1]:
            return arr[i-1]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runnerUpScore(arr))

# sample input: 10
# 2 6 8 3 9 9 0 1 5 1