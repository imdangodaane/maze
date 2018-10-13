#!/usr/bin/env python3
import math
import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


def analysisAndMove(cur_pos, nearest_pos):
    if cur_pos[0] < nearest_pos[0]:
        return 'MOVE RIGHT'
    if cur_pos[0] > nearest_pos[0]:
        return 'MOVE LEFT'
    if cur_pos[1] < nearest_pos[1]:
        return 'MOVE DOWN'
    if cur_pos[1] > nearest_pos[1]:
        return 'MOVE UP'


def findPath(current_pos, resource_pos, ava_move):
    guide = []

    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    path = {}
    r_path = {}

    order = 1
    path[order] = set()
    path[order].add(resource_pos)

    temp_ava_move = list(ava_move)

    while current_pos not in path[order]:
        order += 1
        path[order] = set()
        for pos in path[order - 1]:
            r_path[pos] = set()
            if pos in temp_ava_move:
                temp_ava_move.remove(pos)
            for d in direction:
                temp_pos = (pos[0] + d[0], pos[1] + d[1])
                if temp_pos in temp_ava_move:
                    path[order].add(temp_pos)
                    r_path[pos].add(temp_pos)

    search_key = current_pos

    while search_key != resource_pos:
        for key, values in r_path.items():
            for value in values:
                if value == search_key:
                    search_key = key
                    guide.append(search_key)
                    break

    return (guide, len(guide))


# def findNearest(res_pos, cur_pos, ava_move):
#     _min = 1000000
#     _min_pos = (1000000, 1000000)
#     for i in res_pos:
#         length = len(findPath(cur_pos, i, ava_move))
#         if length < _min:
#             _min = length
#             _min_pos = i
#     return findPath(cur_pos, _min_pos, ava_move)


while True:
    x = input()
    if 'HELLO' in x:
        print('I AM QUI\n')
    if 'YOU ARE' in x:
        my_letter = x[-1]
        print('OK\n')
    if 'MAZE' in x:
        maze = []
        while len(x) > 0:
            x = input()
            maze.append(x)

        normal_resource = []
        rare_resource = []
        available_move = []
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 'o':
                    normal_resource.append((x, y))
                if maze[y][x] == '!':
                    rare_resource.append((x, y))
                if maze[y][x] == my_letter:
                    current_pos = (x, y)
                if maze[y][x] != '#':
                    available_move.append((x, y))
        _min = [[], 1000000]
        for i in normal_resource:
            logging.debug(str(i) + '\n')
        for i in normal_resource:
            logging.debug('current_pos = ' + str(current_pos))
            logging.debug('i = ' + str(i))
            logging.debug('available_move = ' + str(available_move))
            temp = findPath(current_pos, i, available_move)
            logging.debug(str(temp[0]))
            logging.debug(str(temp[1]))
            if temp[1] < _min[1]:
                _min[0] = temp[0]
                _min[1] = temp[1]
                logging.debug(str(_min[0]))
                logging.debug(str(_min[1]))
                logging.debug('End\n')

        # f = open('length', 'a')
        # logging.debug(str(len(my_way)))
        # f.close()
        print(analysisAndMove(current_pos, _min[0][0]) + '\n')
