"""
author : 2015146007 임베디드 시스템과 김세환
date : 2021.09.12
"""

import queue


class State:
    def __init__(self, board_size: int, board: list, col: int = 0) -> None:
        self.board_size = board_size
        self.board = board
        self.col = col

    def get_new_state(self, row: int, col: int = 0):
        new_board = self.board[:]  # list copy
        # 퀸을 두었을때, 해당 행을 퀸을 놓을 수 없는 위치로 표현
        pos = (row * self.board_size) + col
        for i in range(col, self.board_size):
            line = row * self.board_size
            tmp = line + i
            if i == col:
                new_board[tmp] = 2
            else:
                new_board[tmp] = 0
            # 퀸을 두었을 때, 해당 열에 퀸을 놓을 수 없는 위치로 표현
        for i in range(self.board_size):
            line = (i * self.board_size) + col
            # if i >= col:
            if i == row:
                new_board[line] = 2
            else:
                new_board[line] = 0
            # 대각선 퀸을 놓을 수 없는 위치로 처리
        for i in range(col, self.board_size):
            # if col == self.board_size:
            #     break
            line = row * self.board_size + col
            calc = (line + i) - (self.board_size * i)
            if calc > 0:
                new_board[calc] = 0
            calc = (line + i) + (self.board_size * i)
            if (self.board_size * self.board_size) > calc:
                new_board[calc] = 0
        new_board[pos] = 2

        return State(self.board_size, new_board, col)

    def expand(self, col: int = 0) -> list:
        """
        자식노드를 확장하는 메소드
        해당 열의 특정 row가 배치 가능한 row 일 경우만 자식 노드를 확장함
        :param col: 열
        :return: 자식 노드들(State)의 배열
        """
        result = []
        if col < self.board_size:
            for i in range(self.board_size):
                calc = i * self.board_size + col
                if calc >= self.board_size * self.board_size:
                    return []
                if self.board[calc] == 1:
                    result.append(self.get_new_state(i, col))
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
        """
        다음 col 이후에 존재하는 0의 개수를 평가한다.
        :return:
        """
        # return sum([1 if self.board[i] == 0 else 0 for i in range(self.board_size * self.board_size)])  # board size
        ret = 0
        if self.col < self.board_size:
            for i in range(self.col, self.board_size):
                for i2 in range(self.board_size):
                    if self.board[i2 * self.board_size + i] == 0:
                        ret += 1
        return ret

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
        # if current.board.count(2) == N:
        # col = current.col + 1
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
    # s = State(8, [1 for _ in range(8 * 8)])
    # t = s.get_new_state(5, 0)
    # t = t.get_new_state(3, 1)
    # t = t.get_new_state(7, 2)
    # t = t.get_new_state(1, 3)
    # t = t.get_new_state(4, 4)
    # t = t.get_new_state(2, 5)
    # t = t.get_new_state(0, 6)
    # t = t.get_new_state(6, 7)
    # print(t)
