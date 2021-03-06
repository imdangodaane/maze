#!/usr/bin/env python3
import sys


def getMaze():
    maze = []
    x = sys.stdin.readline().rstrip('\n')
    while len(x) > 0:
        maze.append(x)
        x = sys.stdin.readline().rstrip('\n')
    return maze[:-1]


def findStart(maze, my_letter):
    for line in maze:
        if my_letter in line:
            return (line.index(my_letter), maze.index(line))


def findPath(maze, start, my_letter):
    enemy = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'.replace(my_letter, '')
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[start]]
    checked = set(start)
    while queue:
        path = queue.pop(0)
        last_x, last_y = path[-1]
        if maze[last_y][last_x] == '!' and len(path) < 20:
            return path
        elif maze[last_y][last_x] == 'o':
            return path

        for d in direction:
            x, y = last_x + d[0], last_y + d[1]
            if (
                0 <= x < len(maze[0]) and 0 <= y < len(maze) and
                maze[y][x] != '#' and (x, y) not in checked and
                maze[y][x] not in enemy
               ):
                queue.append(path + [(x, y)])
                checked.add((x, y))


def move(start, goal):
    if start[0] < goal[0]:
        return sys.stdout.write('MOVE RIGHT\n\n')
    elif start[0] > goal[0]:
        return sys.stdout.write('MOVE LEFT\n\n')
    elif start[1] < goal[1]:
        return sys.stdout.write('MOVE DOWN\n\n')
    elif start[1] > goal[1]:
        return sys.stdout.write('MOVE UP\n\n')


def evade(maze, start):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in direction:
        x, y = start[0] + d[0], start[1] + d[1]
        if (
            0 <= x < len(maze[0]) and 0 <= y < len(maze) and
            maze[y][x] != '#' and maze[y][x] not in 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
           ):
           return [start, (x, y)]


if __name__ == "__main__":
    while True:
        x = sys.stdin.readline()
        if 'HELLO' in x:
            sys.stdout.write('I AM QUI\n\n')
        if 'YOU ARE' in x:
            my_letter = x[-2]
            sys.stdout.write('OK\n\n')
        if 'MAZE' in x:
            maze = getMaze()
            start = findStart(maze, my_letter)
            path = findPath(maze, start, my_letter)
            if path:
                move(path[0], path[1])
            else:
                path = evade(maze, start)
                move(path[0], path[1])
        if len(x) == 0:
            break
