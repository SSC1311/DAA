import heapq

class Node:
    def _init_(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def _lt_(self, other):
        return self.freq < other.freq

def print_node(node, code=''):
    if node.left is None and node.right is None:  # Leaf node
        print(f"{node.symbol} -> {code}")
        return
    if node.left:
        print_node(node.left, code + '0')
    if node.right:
        print_node(node.right, code + '1')

if _name_ == "_main_":
    print("----- Huffman Coding -----")
    n = int(input("Enter the number of characters: "))
    chars = []
    freq = []
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        f = int(input(f"Enter frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)

    nodes = [Node(freq[i], chars[i]) for i in range(n)]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes for each character:")
    print("--------------------------------")
    print_node(nodes[0])
