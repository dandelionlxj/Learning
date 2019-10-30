# coding=utf-8
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1)
]


def maze_paths(x1, y1, x2, y2):
    """
    用栈来实现
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    stack = [(x1, y1)]
    while (len(stack) > 0):
        curnode = stack[-1]
        if curnode[0]==x2 and curnode[1]==y2:
            for i in stack:
                print(i)
            return True
        for dir in dirs:
            nextnode = dir(curnode[0], curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                stack.append(nextnode)
                maze[nextnode[0]][nextnode[1]] = 2
                break
        else:
            maze[curnode[0]][curnode[1]] = 2
            stack.pop()
    else:
        print('走不通')
        return False

print(maze_path(1,1,8,8))