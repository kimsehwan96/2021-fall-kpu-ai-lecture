import queue


class State:
    def __init__(self, board: list, goal: list, moves: int = 0) -> None:
        self.board = board
        self.moves = moves
        self.goal = goal

    # i1과 i2를 교환하여 새로운 상태 반환

    def get_new_board(self, i1: int, i2: int, moves: int):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    # 자식 노드 확장 및 반환
    def expand(self, moves:int) -> list:
        result = []
        i = self.board.index(0)  # 0는 8-puzzled에서의 빈칸
        # i는 인덱스에 해당하는 값
        # 아래는 일종의 연산자임
        if not i in [0, 1, 2]:  # UP 연산자
            result.append(self.get_new_board(i, i - 3, moves))
        if not i in [0, 3, 6]:  # LEFT 연산자
            result.append(self.get_new_board(i, i - 1, moves))
        if not i in [2, 5, 8]:  # RIGHT 연산자
            result.append(self.get_new_board(i, i + 1, moves))
        if not i in [6, 7, 8]:  # DOWN 연산자
            result.append(self.get_new_board(i, i + 3, moves))
        return result

    def f(self):
        return self.h() + self.g()

    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    def g(self):
        return self.moves

    def __lt__(self, other):
        return self.f() < other.f()

    def __str__(self):
        return "------------ f(n)=" + str(self.f()) + "\n" + \
               "------------ h(n)=" + str(self.h()) + "\n" + \
               "------------ g(n)=" + str(self.g()) + "\n" + \
               str(self.board[:3]) + "\n" + \
               str(self.board[3:6]) + "\n" + \
               str(self.board[6:]) + "\n" + \
               '----------------'


puzzle = [
    1, 2, 3,
    0, 4, 6,
    7, 5, 8]
# 초기 상태

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]
# 목표 상태


open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))

closed_queue = []

moves = 0

while not open_queue.empty():

    current = open_queue.get()
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves + 1
    for state in current.expand(moves):
        if state not in closed_queue:
            open_queue.put(state)
        closed_queue.append(current)
    else:
        print('탐색 실패')