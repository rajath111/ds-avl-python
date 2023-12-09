from typing import Optional


class Node:
    def __init__(self, value, left: 'Node' = None, right: 'Node' = None, height: int = 1) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.height = height



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

        left = 0
        right = 0

        if node.left:
            left = node.left.height

        if node.right:
            right = node.right.height

        return max(left, right) + 1
    

    def _get_balance_factor(self, node: Node) -> int:

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
        C = B.left
        Br = B.right

        # Rotate
        B.left = C
        B.right = A
        A.left = Br

        
        pass

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
        C = B.right
        Bl = B.left
        
        # Rotate
        B.left = A
        B.right = C
        A.right = Bl
        
        return B
        
    
    def _insert_recur(self, node: Node, value) -> Node:
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recur(node.left, value)
        else:
            node.right = self._insert_recur(node.right, value)

        # 1. Update height
        node.height = self._get_node_height(node)

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
                
                pass

        elif balance_factor < -1:
            # Right rotations RR vs RL
            if value >= node.right.value:
                # Perform RR    
                pass
            else:
                # Perform RL
                pass

        return node

    
    