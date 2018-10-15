#!/usr/bin/env python3


def move(start, goal):
    # compare current position to next position to send next MOVE
    if start[0] < goal[0]:
        return 'MOVE RIGHT\n'
    if start[0] > goal[0]:
        return 'MOVE LEFT\n'
    if start[1] < goal[1]:
        return 'MOVE DOWN\n'
    if start[1] > goal[1]:
        return 'MOVE UP\n'


def findPath(maze, start, movable_pos):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp_movable_pos = list(movable_pos)
    temp_movable_pos.remove(start)

    path = []

    level_search = {}
    trace_back = {}

    level = 1
    level_search[level] = set()
    level_search[level].add(start)

    continue_flag = 1
    while continue_flag == 1:
        level += 1
        level_search[level] = set()
        for pos in level_search[level - 1]:
            if maze[pos[1]][pos[0]] == 'o' or maze[pos[1]][pos[0]] == '!':
                end = (pos[0], pos[1])
                path.append(end)
                continue_flag = 0
                break
            else:
                trace_back[pos] = set()
                if pos in temp_movable_pos:
                    temp_movable_pos.remove(pos)
                for d in direction:
                    temp_pos = (pos[0] + d[0], pos[1] + d[1])
                    if temp_pos in temp_movable_pos:
                        level_search[level].add(temp_pos)
                        trace_back[pos].add(temp_pos)

    search_key = end

    while search_key != start:
        for key, values in trace_back.items():
            for value in values:
                if value == search_key:
                    search_key = key
                    path.append(search_key)
                    break
    r_path = []
    for i in range(len(path)):
        r_path.append(path.pop())
    r_path.pop(0)
    return r_path


def guideToInstruction(cur_pos, guide):
    instruction = []
    for pos in guide:
        instruction.append(move(cur_pos, pos))
        cur_pos = pos
    return instruction


instruction = []


while True:
    x = input()
    if 'HELLO' in x:
        print('I AM QUI\n')
    if 'YOU ARE' in x:
        my_letter = x[-1]
        print('OK\n')
    if 'MAZE' in x:
        if len(instruction) > 0:
            print(instruction[0])
            instruction.remove(instruction[0])
        else:
            maze = []
            while len(x) > 0:
                x = input()
                maze.append(x)
            f = open('README.md', 'w')
            f.write('')
            f.close()
            f = open('README.md', 'a')
            for i in maze:
                f.write(str(i) + '\n')
            f.close()
            available_move = []
            for y in range(len(maze)):
                for x in range(len(maze[y])):
                    if maze[y][x] != '#':
                        available_move.append((x, y))
                    if maze[y][x] == my_letter:
                        current_pos = (x, y)

            guide = findPath(maze, current_pos, available_move)
            instruction = guideToInstruction(current_pos, guide)
            print(instruction[0])
            instruction.remove(instruction[0])
