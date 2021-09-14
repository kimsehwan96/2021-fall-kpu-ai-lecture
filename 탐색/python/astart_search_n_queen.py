"""
author : 2015146007 임베디드 시스템과 김세환
date : 2021.09.12
"""

import queue
from copy import deepcopy


# 우선 goal 상태(목표)를 정하고 진행하기 위해서, 8-QUEEN 이라고 가정하고 시작한다.

class State:
    def __init__(self, board_size: int, board: list, col: int = 0) -> None:
        self.board_size = board_size
        self.board = board
        self.col = col

    def get_new_state(self, row: int, col: int = 0):
        new_board = self.board[:]  # list copy
        # 퀸을 두었을때, 해당 행을 퀸을 놓을 수 없는 위치로 표현
        pos = (row * self.board_size) + col
        for i in range(self.board_size):
            line = row * self.board_size
            tmp = line + i
            if i == col:
                new_board[tmp] = 2
            else:
                if i > col:
                    new_board[tmp] = 0
            # 퀸을 두었을 때, 해당 열에 퀸을 놓을 수 없는 위치로 표현
            line = (i * self.board_size) + col
            if i >= col:
                if i == row:
                    new_board[line] = 2
                else:
                    new_board[line] = 0
            # 오른쪽 방향 대각선, 퀸을 놓을 수 없는 위치로 처리
            line = row * self.board_size + col
            # UP SIDE
            calc = (line + i) - (self.board_size * i)
            if calc > 0:
                # if calc != pos:
                new_board[calc] = 0
            calc = (line + i) + (self.board_size * i)
            if (self.board_size * self.board_size - 1) > calc > 0:
                # if calc != pos:
                new_board[calc] = 0
        new_board[pos] = 2

        return State(self.board_size, new_board, col)

    def expand(self, col: int = 0) -> list:
        result = []
        # 8개 각 행에 놓는 것을 연산자로 표현한다.
        if col < self.board_size:
            for i in range(self.board_size):
                if self.board[i * self.board_size + col] == 1:
                    result.append(self.get_new_state(i, col))
            # tmp = self.get_new_state(i, col)
            # if tmp.board[(i * self.board_size) + col] != 0:
            #     result.append(self.get_new_state(i, col))
            # # result.append(tmp)
        return result

    def print_board(self) -> None:
        ret = ""
        for i in range(self.board_size):
            cnt = i * self.board_size
            ret += str(self.board[cnt:cnt + self.board_size])
            ret += "\n"
        return ret

    def f(self):
        return self.h() + self.g()

    def h(self):
        return sum([1 if self.board[i] == 0 else 0 for i in range(self.board_size * self.board_size)])  # board size

    def g(self):
        return self.col

    def __lt__(self, other):
        return self.f() < other.f()

    def __str__(self):
        return "------------ f(n)=" + str(self.f()) + "\n" + \
               "------------ h(n)=" + str(self.h()) + "\n" + \
               "------------ g(n)=" + str(self.g()) + "\n" + \
               self.print_board() + "\n" + \
               "----------------"


# init = [
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     ]
# 초기 상태 8x8 chess board / 1은 퀸을 둘 수 있는 위치라고 표현함.
# 0은 퀸을 둘 수 없는 위치, 2는 퀸을 둔 위치

# goal = [
#     0, 0, 0, 2, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 2, 0,
#     0, 0, 2, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 2,
#     0, 2, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 2, 0, 0, 0,
#     2, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 2, 0, 0
#         ]
# 목표 상태

def check_is_goal(size: int, l: list) -> bool:
    for col in range(size):
        cnt = 0
        for row in range(size):
            if l[row * size + col] == 2:
                cnt += 1
        if cnt == 1:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    N = int(input('input board size N : '))
    init_table = [1 for x in range(N * N)]
    open_queue = queue.PriorityQueue()
    open_queue.put(State(N, init_table))
    closed_queue = []
    col = 0

    while not open_queue.empty():
        current = open_queue.get()
        print(current)
        # if current.board.count(2) == N-1:
        if check_is_goal(N, current.board):
            print('탐색 성공')
            break
        for state in current.expand(col):
            if state not in closed_queue:
                open_queue.put(state)
            closed_queue.append(current)
        else:
            print('탐색 실패')
        col = current.col + 1
    # s = State(8, [1 for x in range(64)])
    # t = s.get_new_state(0, 0)
    # # print(t)
    # tt = t.get_new_state(6,1)
    # print(tt)
    # # ns = t.expand(1)
    # # for v in ns:
    # #     print(v)
    # # # print(t)
    # # t2 = t.get_new_state(3,1)
    # # print(t2)