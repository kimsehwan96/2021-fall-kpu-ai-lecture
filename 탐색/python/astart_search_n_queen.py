"""
author : 2015146007 임베디드 시스템과 김세환
date : 2021.09.12
"""

import queue

class State:
    def __init__(self, board_size: int, board: list, goal: list, col: int = 0) -> None:
        self.board_size = board_size  # if 4 -> 4x4 = array of int 16
        self.board = board
        self.col = col
        self.goal = goal

    def get_new_state(self, row: int, col: int = 0):
        # row / col 에 해당하는 좌표에 체스말을 두었을 때, 현재 퀸의 위치와 다음 퀸을 둘 수 있고 없고의 상태를 표현
        new_board = self.board[:]  # 리스트 복사
        queen_pos = row * self.board_size + col
        new_board[queen_pos] = 2 #퀸을 두었음
        # 이후 나머지 보드에서 퀸을 둘 수 없는 칸을 처리하기

        #위,아래쪽 처리
        for i in range(self.board_size):
            calc = col + self.board_size * i
            if calc != queen_pos:
                new_board[calc] = 0
        #좌, 우 처리
        for i in range(self.board_size):
            calc = i + row * self.board_size
            if calc != queen_pos:
                new_board[calc] = 0
        #대각선 처리
        return new_board


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


if __name__ == '__main__':
    print('input N :')
    N = int(input())
    init_board = [1 for x in range(N * N)]
    s = State(N, init_board, [], 0)
    n = State(N, s.get_new_state(3, 0), [])
    t = State(N, n.get_new_state(1, 1), [])
    print(t)
