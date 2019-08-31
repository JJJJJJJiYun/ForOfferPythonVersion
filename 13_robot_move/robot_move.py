# -*- encoding: utf-8 -*-


def max_robot_move(m, n, limit):
    if m <= 0 or n <= 0 or limit <= 0:
        return 0
    visited = []
    for i in range(0, m):
        visited.append([])
        for j in range(0, n):
            visited[i].append(False)
    return helper(0, 0, visited, limit)


def helper(i, j, visited, limit):
    if i < 0 or i >= len(visited) or j < 0 or j >= len(
            visited[0]) or visited[i][j] or digit_plus(i, j) > limit:
        return 0
    visited[i][j] = True
    count = 1 + helper(i - 1, j, visited, limit) + \
            helper(i + 1, j, visited, limit) + \
            helper(i, j - 1, visited, limit) + \
            helper(i, j + 1, visited, limit)
    return count


def digit_plus(a, b):
    a = str(a)
    b = str(b)
    result = 0
    for ch in a:
        result += int(ch)
    for ch in b:
        result += int(ch)
    return result


if __name__ == '__main__':
    print max_robot_move(20, 20, 15)
