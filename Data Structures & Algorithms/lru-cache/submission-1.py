class LRUCache:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        node = self.Node(key, value)
        self.hash_map[key] = node
        self._add_to_front(node)

        if len(self.hash_map) > self.capacity:
            removed_node = self.tail.prev
            self._remove(removed_node)
            del self.hash_map[removed_node.key]