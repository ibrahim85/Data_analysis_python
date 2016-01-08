def distributionSorter(data, grid):

    distribution = [0] * len(grid)  #just equivalent to Matlab zeros(length(grid), 1)
    data = sorted(data)  #this helps to reduce the computation time.
    # We won't rescan the whole grid vector but start from where the previous element left our cursor
    j = 0

    for i in range(0, len(data)):
        while data[i] > grid[j]:
            j += 1
            if j == len(grid):
                j -= 1
                break

        distribution[j] += 1

    return distribution

