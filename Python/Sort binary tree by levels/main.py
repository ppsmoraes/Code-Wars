class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node: Node | None) -> list:
    result: list = []
    nodes_list: list[Node] = []

    if isinstance(node, Node):
        nodes_list.append(node)

    while len(nodes_list) > 0:
        node_cache: Node = nodes_list[0]

        result.append(node_cache.value)

        if isinstance(node_cache.left, Node):
            nodes_list.append(node_cache.left)

        if isinstance(node_cache.right, Node):
            nodes_list.append(node_cache.right)

        nodes_list.remove(node_cache)

    return result


def tests() -> None:
    node: Node = Node(
        Node(None, Node(None, None, 3), 8),
        Node(None, Node(None, Node(None, None, 7), 5), 4),
        1,
    )
    print(tree_by_levels(node))


if __name__ == '__main__':
    tests()
