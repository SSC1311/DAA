import heapq

class Node:
    """Huffman tree node"""
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    # heapq needs nodes to be comparable; compare by frequency
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(symbols, freqs):
    """
    Build Huffman tree from lists of symbols and corresponding frequencies.
    Returns the root node of the Huffman tree.
    """
    heap = []
    # create a heap of leaf nodes
    for s, f in zip(symbols, freqs):
        heapq.heappush(heap, Node(f, symbol=s))

    # combine two smallest nodes until one node remains (the root)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        combined = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, combined)

    return heap[0] if heap else None


def generate_codes(root):
    """
    Traverse the Huffman tree and generate binary codes for each symbol.
    Returns a dict: {symbol: code}.
    """
    codes = {}

    def _generate(node, code_str):
        if node is None:
            return
        # If leaf node, assign code
        if node.left is None and node.right is None:
            codes[node.symbol] = code_str or "0"  # handle single-symbol edge-case
            return
        _generate(node.left, code_str + "0")
        _generate(node.right, code_str + "1")

    _generate(root, "")
    return codes


def encode(message, codes):
    """Encode the message (string of symbols) using the provided codes dict."""
    return "".join(codes[ch] for ch in message)


def decode(encoded_str, root):
    """Decode the encoded string back to original message using the Huffman tree."""
    result = []
    node = root
    for bit in encoded_str:
        node = node.left if bit == "0" else node.right
        # if leaf
        if node.left is None and node.right is None:
            result.append(node.symbol)
            node = root
    return "".join(result)


# ------------------- Demo / Example -------------------
if __name__ == "__main__":
    # example symbols and frequencies
    symbols = ['a', 'b', 'c', 'd', 'e', 'f']
    freqs   = [5,   9,   12,  13,  16,  45]

    # build tree and codes
    root = build_huffman_tree(symbols, freqs)
    codes = generate_codes(root)

    print("Huffman Codes:")
    for s in sorted(codes):  # sorted for predictable order
        print(f"  {s} -> {codes[s]}")

    # example encoding & decoding
    message = "face"  # sample message (sequence of symbols)
    encoded = encode(message, codes)
    decoded = decode(encoded, root)

    print("\nExample:")
    print(f"  message: {message}")
    print(f"  encoded: {encoded}")
    print(f"  decoded: {decoded}")
