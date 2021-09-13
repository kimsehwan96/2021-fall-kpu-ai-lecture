"""
author : 2015146007 임베디드 시스템과 김세환
date : 2021.09.12
"""

import queue
from copy import deepcopy
# 우선 goal 상태(목표)를 정하고 진행하기 위해서, 8-QUEEN 이라고 가정하고 시작한다.

class State:
    def __init__(self, board: list, goal: list, col: int = 0) -> None:
        self.board = board
        self.col = col
        self.goal = goal

    def get_new_state(self, board, row, col: int = 0):
        new_board = deepcopy(self.board) #list copy
        # ...
        return State(new_board, self.goal, col)

    def expand(self, col: int) -> list:
        result = []
        pass

    def print_board(self) -> None:
        ret = ""
        for i in range(self.board_size):
            cnt = i * self.board_size
            ret += str(self.board[cnt:cnt+self.board_size])
            ret += "\n"
        return ret

    def __str__(self):
        return "------------ f(n)=" + "\n" + \
               "------------ h(n)=" + "\n" + \
               "------------ g(n)=" + "\n" + \
               self.print_board() + "\n" + \
               "----------------"

init = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    ]
# 초기 상태 8x8 chess board / 1은 퀸을 둘 수 있는 위치라고 표현함.
# 0은 퀸을 둘 수 없는 위치, 2는 퀸을 둔 위치

goal = [
    0, 0, 0, 2, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 2, 0,
    0, 0, 2, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 2,
    0, 2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 2, 0, 0, 0,
    2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 2, 0, 0
        ]
# 목표 상태

if __name__ == '__main__':
    pass