def CountDominantCells(grid):
    count = 0
    steps = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbours = 0
            count_temp = 0
            for step in steps:
                if all([len(grid) > i + step[0] >= 0, len(grid[0]) > j + step[1] >= 0 ]):
                    neighbours += 1
                    print(i,j,step,grid[i][j] , grid[i + step[0]][j + step[1]])
                    if grid[i][j] > grid[i + step[0]][j + step[1]]:
                        count_temp += 1
            if neighbours == count_temp:
                count += 1

    return count

if __name__ == '__main__':
    n,m = map(int, input().split())

    grid = []

    for _ in range(n):
        grid.append(list(map(int,input().split())))

    print(CountDominantCells(grid))