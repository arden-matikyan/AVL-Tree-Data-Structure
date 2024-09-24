import json
from typing import List

# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key        = None,
                  value      = None,
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.value      = value
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "k": node.key,
            "v": node.value,
            "l": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr)

# Height of (sub)tree rooted at root.
def height(root: Node) -> int:
   
    if root is None:
        return -1; 

    leftchildHeight = height(root.leftchild)
    rightchildHeight = height(root.rightchild)
    return max(leftchildHeight, rightchildHeight)+1
    

# Insert.
def insert(root: Node, key: int, value: str) -> Node:
    # For the tree rooted at root, insert the given key and return the root node.
    # The key is guaranteed to not be in the tree.
    
    # change insertion to not return early 

    if root is None: 
        return Node(key, value, None, None) 
    elif key > root.key: 
        root.rightchild = insert(root.rightchild, key, value)
    else: 
        root.leftchild = insert(root.leftchild, key, value)
    

    balance = searchForInbalance(root)
    
    # print("balance: ", balance)

    # Left Left  Heavy - rotate right 
    if balance > 1 and key < root.leftchild.key:
        return rotateRight(root)

    # left right heavy - left rotate followed by a right rotate 
    if balance > 1 and key > root.leftchild.key:
        root.leftchild = rotateLeft(root.leftchild)
        return rotateRight(root)   

    # right right heavy - rotate left 
    if balance < -1 and key > root.rightchild.key:
        return rotateLeft(root)

    # right left heavy - right rotate followed by a left rotate 
    if balance < -1 and key < root.rightchild.key:
        root.rightchild = rotateRight(root.rightchild)
        return rotateLeft(root)

    return root

def rotateRight(root: Node):
    

    #print("root: ", root.key)

    piv = root.leftchild
    pivR = piv.rightchild
 
    # Perform rotation
    piv.rightchild = root
    root.leftchild = pivR
 
    return piv


def rotateLeft(root: Node):

    piv = root.rightchild
    pivL = piv.leftchild
 
    # Perform rotation
    piv.leftchild = root
    root.rightchild = pivL

    return piv

def searchForInbalance(root: Node):

    if root is None: 
        return 0 
    
    lh = height(root.leftchild)
    # if lh < 0:
    #     lh = 0 

    rh = height(root.rightchild)
    # if rh < 0:
    #     rh = 0 

    #print("rh ", rh)
    #print("lh ", lh)
    return lh - rh
    
# Bulk Delete.
def delete(root: Node, keys: List[int]) -> Node:

    #print(keys)
    # do a search of each item in keys list and tag nodes to be deleted 
    for i in keys: 
        current = root 
        while i != current.key: 
            if i < current.key: 
                current = current.leftchild
            else: 
                current = current.rightchild
        current.value = "-----"
    
    # first iterate through tree and collect non tagged nodes 
    def collect(current: Node): 

        if current.leftchild is not None:
            collect(current.leftchild)

        if current.value != "-----":
            newkeys.append(current.key)
            newvalues.append(current.value)
        
        if current.rightchild is not None:
            collect(current.rightchild)
    
    newkeys = [] 
    newvalues = [] 
    collect(root)
    

    root = None 

    if len(newkeys) != 0: 
        root = Node(newkeys[0], newvalues[0], None, None)
    
    for index in range(1,len(newkeys)):
        #print(newkeys[index],newvalues[index])
        root = insert(root, newkeys[index], newvalues[index])

    return root

def findnext(root: Node) -> Node: 

    current = root 
    parent = root 
    if root.rightchild is None: 
        return None 
    else:
        parent = current 
        current = current.rightchild
        while current.leftchild is not None:
            current = current.leftchild 

    return current 


# Search.
def search(root: Node, search_key: int) -> str:
    
    current = root 
    ct = 0 
    while (current is not None and search_key != current.key): 
        ct += 1 
        if search_key < current.key: 
            current = current.leftchild
        else: 
            current = current.rightchild

    if current is None: 
        return json.dumps([ct,"None"])
    else:
        return json.dumps([ct+1,current.value])

   

# Range Query.
def rangequery(root: Node, x0: int, x1: int) -> List[str]:
    
    values = [] 
    def rq(current: Node, x0: int, x1: int, vals: List[str]): 
        if current is None:
            return 
        if (x0 <= current.key <= x1):
            values.append(current.value)
            rq(current.leftchild, x0, x1, vals)
            rq(current.rightchild, x0, x1, vals)
        elif (x0 > current.key):
            rq(current.rightchild, x0, x1, vals)
        else: 
            rq(current.leftchild, x0, x1, vals)

    rq(root, x0, x1, values)
    return values
