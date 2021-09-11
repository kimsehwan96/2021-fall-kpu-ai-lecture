# 8-Puzzle 탐색 예제 코드

class State(object):
    def __init__(self, board: list, goal: list, moves: int = 0) -> None:
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves: int):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        # 인자로 주어진 i1 인덱스에 해당하는 값과, i2에 해당하는 값을 반전시킨다.
        # 그리고 State(자기자신)을 반환한다.
        return State(new_board, self.goal, moves)

    def expand(self, moves: int):
        result = []
        i = self.board.index(0) # 0는 8-puzzled에서의 빈칸
        # i는 인덱스에 해당하는 값
        # 아래는 일종의 연산자임
        if not i in [0, 1, 2]: #UP 연산자
            result.append(self.get_new_board(i, i - 3, moves))
        if not i in [0, 3, 6]: #LEFT 연산자
            result.append(self.get_new_board(i, i - 1, moves))
        if not i in [2, 5, 8]: #RIGHT 연산자
            result.append(self.get_new_board(i, i + 1, moves))
        if not i in [6, 7, 8]: #DOWN 연산자
            result.append(self.get_new_board(i, i + 3, moves))
        return result
        # 0 1 2
        # 3 4 5
        # 6 7 8
    def __str__(self):
        return str(self.board[:3]) + "\n" + \
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

open_queue = []
open_queue.append(State(puzzle, goal))

closed_queue = []
moves = 0

while len(open_queue) != 0:
    current = open_queue.pop(0)
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves + 1
    closed_queue.append(current)
    for state in current.expand(moves):
        if (state in closed_queue) or (state in open_queue):
            continue
        else:
            open_queue.append(state)
