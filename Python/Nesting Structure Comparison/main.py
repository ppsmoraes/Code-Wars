def same_structure_as(original: list, other: list) -> bool:
    if not (isinstance(original, list) and isinstance(other, list)):
        return False

    if len(original) != len(other):
        return False

    for i, j in zip(original, other):
        if isinstance(i, list):
            if not isinstance(j, list):
                return False

            if not same_structure_as(i, j):
                return False

        elif isinstance(j, list):
            return False

    return True


def tests():
    print(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)
    print(same_structure_as([],1), False)


if __name__ == '__main__':
    tests()
