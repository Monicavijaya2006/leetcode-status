from collections import defaultdict

class Node : 
    def __init__(self,key = 0 , val = 0) : 
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class NodeList : 
    def __init__(self) : 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addNode(self,node) : 
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        first.prev = node
        node.next = first

        self.size += 1
    
    def removeNode(self,node) : 
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def removeLast(self) : 
        if self.size == 0 : 
            return
        node = self.tail.prev
        self.removeNode(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.key_node = {}
        self.freq_table = defaultdict(NodeList)

    def updateFrequency(self,node) : 
        old_freq = node.freq

        self.freq_table[old_freq].removeNode(node)
        if old_freq == self.minFreq and self.freq_table[old_freq].size == 0 : 
            self.minFreq += 1
        
        node.freq += 1
        self.freq_table[node.freq].addNode(node)

    def get(self, key: int) -> int:
        if key not in self.key_node : 
            return -1
        
        node = self.key_node[key]
        self.updateFrequency(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node : 
            node = self.key_node[key]
            node.val = value
            self.updateFrequency(node)
            return
        if len(self.key_node) == self.capacity : 
            lfu = self.freq_table[self.minFreq].removeLast()
            del self.key_node[lfu.key]
        
        node = Node(key,value)
        self.key_node[key] = node
        self.freq_table[1].addNode(node)
        self.minFreq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)