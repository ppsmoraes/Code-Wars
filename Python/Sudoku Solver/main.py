def get_block_values(puzzle: list[list[int]], x: int, y: int):
    result: list[int] = []

    for row in range(9):
        for col in range(9):
            if row // 3 == x // 3 and col // 3 == y // 3:
                result.append(puzzle[row][col])

    return result


def get_possible_values(puzzle: list[list[int]], x: int, y: int) -> set[int]:
    answers_set: set[int] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    answers_set -= set(puzzle[x])
    answers_set -= set([row[y] for row in puzzle])
    answers_set -= set(get_block_values(puzzle, x, y))

    return answers_set


def sudoku(puzzle: list[list[int]]):
    queue: list[tuple[int, int]] = []

    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == 0:
                queue.append((i, j))

    while queue:
        for i, j in queue:
            ans: set[int] = get_possible_values(puzzle, i, j)
            if len(ans) == 1:
                puzzle[i][j] = ans.pop()
                queue.remove((i, j))

    return puzzle


def tests():
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    result = sudoku(puzzle)

    excepted_ressult = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    return result == excepted_ressult


if __name__ == '__main__':
    print(tests())
