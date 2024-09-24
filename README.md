Details

The functions should do the following:

• def height(root: Node) -> int:

Calculate the height of the tree rooted at root.

• def insert(root: Node, key: int, value: str) -> Node:

Insert a key-value pair and rebalance the tree. The key is guaranteed to not exist.

• def delete(root: Node, keys: List[int]) -> Node:

Perform a bulk deletion of all the nodes whose keys are in the list. They are all guaranteed to
exist. Do this by first tagging all the corresponding nodes somehow, then perform an in-order
traversal of the tree, ignoring the tagged nodes, to get an ordered list of key-value pairs which
remain, then completely rebuild the tree using that list and insert.

• def search(root: Node, search_key: int) -> str:

For the tree rooted at root, calculate the number of keys on the path from the root to the
search key, including the search key, and the value associated with the search key. Return the
json stringified list of the form [number of keys, corresponding search value]. If the
search key is not in the tree return [number of keys, None].

• def rangequery(root: Node, x0: int, x1: int) -> List[str]:

Perform a range query for all keys in the tree between x0 and x1 inclusive. Return a list of
corresponding values. Careful! Do this by creating a list and appending recursively as follows,
starting at the root: If the key is in the interval, append its value and then recursively look at
both children. If the key is greater than x1 then recursively look at the left child and if the
key is less than x0 then recursively look at the right child. Return the list of corresponding
values. Note that if you do this in a different way you may get an incorrectly ordered list
