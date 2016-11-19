import heapq
class PriorityQue(object):
    def __init__(self, nodes=[]):
        self.heap = []
        self.entry_finder = dict()
        for node in nodes:
            entry = [node.value, node]
            self.add_node2(entry)
        self.REMOVED = '<remove_marker>'

    def add_node(self,node,priority=0):
        if node in self.entry_finder:
            self.remove_node(node)
        entry = [node.value,node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap,entry)

    def remove_node(self,node):
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED


    def pop_node(self):
        while self.heap:
            node = heapq.heappop(self.heap)[-1]
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return node
        raise KeyError('pop from an empty priority queue')