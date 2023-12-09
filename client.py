from typing import Any, List
from avl import Avl, Node


def inroder_traversal(node: Node, result: List[Any]) -> None:

    if node is None:
        return 
    
    inroder_traversal(node.left, result)
    result.append(node.value)
    inroder_traversal(node.right, result)



if __name__ == '__main__':
    array = [19, 2, 3, 6, 8, 19, 10, 28, 5, 2, 37, 87, 90]

    avl = Avl()

    for val in array:
        avl.insert(val)

    result = []
    inroder_traversal(avl.get_root(), result)

    print('Inorder traversal of AVL tree: ', result)
    print('Height is : ', avl.get_height())