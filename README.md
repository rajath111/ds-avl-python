# ds-avl-python
Implementation of AVL tree using Python

AVL is a type of self balancing tree. The time required for searching in a Binary Search Tree depends on the height of the tree. For a perfectly balanced tree time complexity for search operation in O(log (N) ). But if we do not construct a perfectly balanced tree, then it will take more time to search for a key in tree. For example, for completely skewed tree either in left or right direction the search operation takes O(N) time. So to summarize, the average time complexity for search operation in Simple Binary Search tree is O(log n) and worst case scenario is O(N).


If the BST is balanced than the search operation is efficient. There are multiple algorithms to make given tree balanced. Some are AVL and Red Black trees.


AVL self balances itself by roating the nodes when the nodes are not balanced. It uses metric called balancing factor.

```
    Balance factor = (height of left sub tree) - (height of right sub tree)
```

If |Balance factor| <= 1, then the tree is balanced. Else, the tree is not balanced on that node and we need to perform rotations to make the tree balanced.


## Insertion 
Start inserting like any other BST using recursive approach. The new node will be a leaf node, so all its ancestor's height will have impact because of this. 

At each node while traversing up, perform the following operations.

1. Update the height of the current node
2. Get balancing factor of the current node
3. If balancing factor >= 1
   1. Then the new node is inserted in left subtree
   2. If new node value is on left of left sub tree, then perform LL rotation (Remember we are working with Binary Search Tree)
   3. Else perform LR rotation

4. Else
   1. Then the new node is inserted in right subtree
   2. If new node value is on right of the right sub tree, then perform RR rotation 
   3. Else perform RL rotation



### Visualization of LL(Right rotation) and RR(Left rotation)
