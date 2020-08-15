class Node:
    def __init__(self, char=None, left=None, right=None, count=None):
        self.char = char
        self.left = left
        self.right = right
        self.count = count

class Huffman:
    def __init__(self, ):
        self.root = None
        self.encode_dict = {}
        self.decode_dict = {}

    def encode(self, data):
        unique_data = set(data)
        nodes = []
        for i in unique_data:
            nodes.append(Node(char=i, count=data.count(i)))

        while len(nodes) >= 2:
            temp = []
            for _ in range(2):
                min_node = min(nodes, key=lambda x:x.count)
                temp.append(min_node)
                nodes.remove(min_node)
            integrated_note = Node(char=None, count=temp[0].count+temp[1].count, left=temp[1], right=temp[0])
            nodes.append(integrated_note)
        self.tree = nodes[0]
        self.recursive_code(self.tree, "")
        s = ""
        for c in data:
            s += self.encode_dict[c]
        return s


    def recursive_code(self, node, s):
        if not isinstance(node, Node):
            return
        if node.char is not None:
            self.encode_dict[node.char] = s
            self.decode_dict[s] = node.char
            return

        self.recursive_code(node.right,s + "1")
        self.recursive_code(node.left, s+ "0")

    def decode(self, data):
        res = ""
        s = ""
        for bit in data:
            s += bit
            if s in self.decode_dict:
                res += self.decode_dict[s]
                s = ""
            else:
                pass
        return res

        return res


h = Huffman()
x = h.encode("AABCCDEEE")
print(x, len(x))
d = h.decode(x)
print("decoded:", d)
