import collections

# --- TASK 1: BINARY SEARCH TREE (BST) ---
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None: node.left = BSTNode(key)
            else: self._insert(node.left, key)
        elif key > node.key:
            if node.right is None: node.right = BSTNode(key)
            else: self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key: return node is not None
        if key < node.key: return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: return node
        if key < node.key: node.left = self._delete(node.left, key)
        elif key > node.key: node.right = self._delete(node.right, key)
        else:
            # Cases: No child or One child
            if node.left is None: return node.right
            elif node.right is None: return node.left
            # Case: Two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        curr = node
        while curr.left: curr = curr.left
        return curr

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        print("Inorder Traversal:", res)

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.key)
            self._inorder(node.right, res)

# --- TASK 2: GRAPH (ADJACENCY LIST + BFS/DFS) ---
class Graph:
    def __init__(self):
        self.adj = collections.defaultdict(list)

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def print_adj_list(self):
        print("Graph Adjacency List:")
        for node in sorted(self.adj.keys()):
            print(f"  {node}: {self.adj[node]}")

    def bfs(self, start):
        visited = set()
        queue = collections.deque([start])
        visited.add(start)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v, w in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        print(f"BFS Traversal from {start}: {' -> '.join(order)}")

    def dfs(self, start):
        visited = set()
        order = []
        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, w in self.adj[u]:
                if v not in visited: _dfs(v)
        _dfs(start)
        print(f"DFS Traversal from {start}: {' -> '.join(order)}")

# --- TASK 3: HASH TABLE (SEPARATE CHAINING) ---
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key: return pair[1]
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                self.table[idx].pop(i)
                return True
        return False

    def display(self):
        print("Hash Table State:")
        for i, bucket in enumerate(self.table):
            print(f"  Bucket {i}: {bucket}")

# --- MAIN RUNNER (TEST PLAN) ---
if __name__ == "__main__":
    print("=== TASK 1: BST TEST PLAN ===")
    bst = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]: bst.insert(x)
    bst.inorder()
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))
    print("\nDeleting 20 (Leaf):")
    bst.delete(20); bst.inorder()
    print("Deleting 60 (Node with Child 65):")
    bst.insert(65); bst.delete(60); bst.inorder()
    print("Deleting 50 (Root/Two Children):")
    bst.delete(50); bst.inorder()

    print("\n=== TASK 2: GRAPH TEST PLAN ===")
    g = Graph()
    edges = [('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3), ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6), ('C','F',8)]
    for u, v, w in edges: g.add_edge(u, v, w)
    g.print_adj_list()
    g.bfs('A')
    g.dfs('A')

    print("\n=== TASK 3: HASH TABLE TEST PLAN ===")
    ht = HashTable(5)
    for k in [10, 15, 20, 7, 12]: ht.insert(k, f"Val_{k}")
    ht.display()
    print("Get 15:", ht.get(15))
    print("Deleting 15 (Collided Bucket):")
    ht.delete(15)
    ht.display()