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

    def get_new_state(self, row: int, col: int = 0):
        new_board = deepcopy(self.board) #list copy
        # 퀸을 두었을때, 해당 행을 퀸을 놓을 수 없는 위치로 표현
        pos = row * 8 + col
        for i in range(8):
            line = row * 8
            tmp = line + i
            if i == col:
                new_board[tmp] = 2
            else:
                if i > col:
                    new_board[tmp] = 0
        # 퀸을 두었을 때, 해당 열에 퀸을 놓을 수 없는 위치로 표현
            line = (i * 8) + col
            if i == row:
                new_board[line] = 2
            else:
                new_board[line] = 0
        # 오른쪽 방향 대각선, 퀸을 놓을 수 없는 위치로 처리
            line = row * 8 + col
            #UP SIDE
            calc = (line + i) - (8 * i)
            if calc >= 0:
                if calc != pos:
                    new_board[calc] = 0
            calc = (line + i) + (8 * i)
            if calc <= 47:
                if calc != pos:
                    new_board[calc] = 0
        new_board[pos] = 2
            
        return State(new_board, self.goal, col)

    def expand(self, col: int) -> list:
        result = []
        #8개 각 행에 놓는 것을 연산자로 표현한다.
        for i in range(8):
            tmp = self.get_new_state(i, col)
            if tmp.board[i * 8 + col] != 0:
                result.append(self.get_new_state(i, col))
            else:
                pass
        return result

    def print_board(self) -> None:
        ret = ""
        for i in range(8):
            cnt = i * 8
            ret += str(self.board[cnt:cnt+8])
            ret += "\n"
        return ret

    def f(self):
        return self.h() + self.g()
    
    def h(self):
        return sum([1 if self.board[i] == 1 else 0 for i in range(48)]) # board size
    
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
    open_queue = queue.PriorityQueue()
    # open_queue.put(State(init, goal))
    s = State(init, goal)
    init_state = s.get_new_state(6, 0)
    open_queue.put(State(init_state.board, goal))
    closed_queue = []
    col = 1
    tmp = 0

    #최초 퀸은 임의로 넣은 뒤 시작한다.
    
    while not open_queue.empty():
        current = open_queue.get()
        print(current)
        if current.board == goal:
            print('탐색 성공')
            break
        col = current.col + 1
        for state in current.expand(col):
            if state not in closed_queue:
                open_queue.put(state)
            closed_queue.append(current)
        else:
            print('탐색 실패')