"""
游戏使用无限大小的矩形网格，其中每个网格都是空的或被有机体占据。 被占用的细胞是活的，而空的细胞是死的。

游戏在特定时期内进行，每一轮都会根据当前配置中生物体的排列创建一个新的世代。

下一代网格的状态，是通过将以下四个基本规则应用于当前配置的每个网格来确定的：

如果一个细胞还活着并且有两个或三个活着的邻居，那么该细胞在下一代中仍然活着；

一个没有活邻居或只有一个活邻居的活细胞会在下一代死于孤立；

有四个或更多活邻居的活细胞会因下一代人口过剩而死亡；

一个只有三个活着的邻居的死细胞会导致出生并在下一代中存活；
"""

board=[[1,0,0],[1,0,0],[1,0,0]]

# 邻居数组为给定的单元格找到8个相邻的单元格
neighbors =[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

rows=len(board)
cols=len(board[0])

# 创建一个原始板的副本
copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

# 逐个单元地迭代
for row in range(rows):
    for col in range(cols):

        # 对于每个单元计算邻居的数量
        live_neighbors = 0
        for neighbor in neighbors:

            r = (row+neighbor[0])
            c = (col+neighbor[1])

            # 检查相邻细胞的有效性，以及它是否原来是一个活细胞
            # 评估是针对副本进行的，因为它永远不会更新。
            if(r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                live_neighbors += 1

        # 规则1或规则3
        if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
            board[row][col] = 0
        # 规则4
        if copy_board[row][col] == 0 and live_neighbors == 3:
            board[row][col] = 1

print(board)