class Solution:
    def lengthLongestPath(self, _input: str) -> int:
        global _max
        _max = 0
    
        class Node:
            def __init__(self, value, path='',depth = 1):
                global _max
                nodes = re.split('\\n' + ("\\t" * depth) + '(?!\W)', value)
                
                self.name = nodes[0]
                
                travel =( path + '-'+ self.name ) if depth > 1 else self.name
    
                if len(travel) > _max and '.' in self.name:
                    _max = len(travel)
                    
                for child in nodes[1:]:
                    d = depth+1
                    Node(child, travel, d)

        for root in re.split('\\n(?!\W)', _input.replace(" ", 'x')):
            Node(root)
        return _max
