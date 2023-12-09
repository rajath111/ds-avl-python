from typing import Any, List
from avl import Avl, Node


def inorder_traversal(node: Node, result: List[Any]) -> None:

    if node is None:
        return 
    
    inorder_traversal(node.left, result)
    result.append(node.value)
    inorder_traversal(node.right, result)



def preorder_traversal(node: Node, result: List[Any]) -> None:

    if node is None:
        return 
    
    result.append(node.value)
    preorder_traversal(node.left, result)
    preorder_traversal(node.right, result)



if __name__ == '__main__':
    '''
                                    8
                        2
        2
    3              
    '''
    array = [19, 2, 3, 6, 8, 19, 10, 28, 5, 2, 37, 87, 90, 43, 56, 22, 43, 23, 56, 21, 85, 86, 23, 54, 11, 2, 3, 5, 6, 35, 432, 873, 432, 546, 232, 545, 218, 3456, 47, 87, 78, 634, 467, 652, 654, 827]

    avl = Avl()

    for val in array:
        avl.insert(val)

    result = []
    inorder_traversal(avl.get_root(), result)

    print('Inorder traversal of AVL tree: ', result, len(result))

    result = []
    preorder_traversal(avl.get_root(), result)

    print('Pre order of AVL: ', result)

    print('Height is : ', avl.get_height())