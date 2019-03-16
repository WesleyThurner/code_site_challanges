if __name__ == '__main__':
    # input number of variables
    n = int(input())
    # input all intergets 
    arr = map(int, input().split())
    # change to list
    scores = list(arr)
    # find top score
    top = max(scores)
    # remove all occurrences of top score
    scores = list(filter((top).__ne__, scores))
    # sort, to print easier
    scores.sort()
    # print last item in list
    print(scores[-1])
