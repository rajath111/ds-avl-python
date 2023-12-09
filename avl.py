from typing import Any, List, Optional

class Node:
    def __init__(self, value, left: 'Node' = None, right: 'Node' = None, height: int = 1) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.height = height


    def __str__(self) -> str:
        return f'Node({self.value})'


class Avl:

    def __init__(self) -> None:
        self.root: Node = None


    def get_root(self) -> Optional[Node]:
        return self.root

    
    def get_height(self) -> int:
        return self._get_height_recur(self.root)

    
    def _get_height_recur(self, node: Node) -> int:
        if node is None:
            return 1
        
        return max(self._get_height_recur(node.left), self._get_height_recur(node.right)) + 1


    def insert(self, value) -> Node:

        self.root = self._insert_recur(self.root, value)
        return self.root

    
    def _get_node_height(self, node: Node) -> int:

        if node == None:
            return 0

        return node.height
    

    def _get_balance_factor(self, node: Node) -> int:
        if node == None:
            return 0
        return self._get_node_height(node.left) - self._get_node_height(node.right)

    
    def _rotate_right(self, node: Node) -> Node:
        '''
            Given any node, It will be rotated in right direction.
            Let A be the given node. We are intrested in A, B and C nodes. Where B is left of A and C is left of B.
            So, children for following nodes are:
                A -> B, Ar
                B -> C, Br
                C -> Cl, Cr
            
            After rotation:
                B -> C, A
                A -> Br, Ar
                C -> Cl, Cr
        '''
        A = node
        B = A.left
        Br = B.right

        # Rotate
        B.right = A
        A.left = Br

        # Order is important. Because first we need to update height of child and then its parent
        self._update_height(A)
        self._update_height(B)
        
        return B


    def _update_height(self, node: Node) -> None:
        node.height = max(self._get_node_height(node.left), self._get_node_height(node.right)) + 1


    def _rotate_left(self, node: Node) -> Node:
        '''
            Given any node, It will be rotated in right direction.
            Let A be the given node. We are intrested in A, B and C nodes. Where B is right of A and C is right of B.
            So, children for following nodes are:
                A -> Al, B
                B -> Bl, C
                C -> Cl, Cr
            
            After rotation:
                B -> A, C
                A -> Al, Bl
                C -> Cl, Cr
        '''
        A = node
        B = A.right
        Bl = B.left
        
        # Rotate
        B.left = A
        A.right = Bl

        self._update_height(A)
        self._update_height(B)
        return B
        
    
    def _insert_recur(self, node: Node, value) -> Node:
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recur(node.left, value)
        elif value > node.value:
            node.right = self._insert_recur(node.right, value)
        else:
            return node

        # 1. Update height
        node.height = max(self._get_node_height(node.left), self._get_node_height(node.right)) + 1

        # 2. Find balace factor
        balance_factor = self._get_balance_factor(node)

        # 3. Perform rotations
        if balance_factor > 1:
            # Left rotations LL vs LR

            if value < node.left.value:
                # Perform LL
                return self._rotate_right(node)
            else:
                # Perform LR
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        elif balance_factor < -1:
            # Right rotations RR vs RL
            if value > node.right.value:
                # Perform RR    
                return self._rotate_left(node)
            else:
                # Perform RL
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node
