class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        cur = self.head.next
        for _ in range(index):
            if cur.next is None:
                return -1
            cur = cur.next
        if cur:
            return cur.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        cur = self.head
        for _ in range(index):
            if cur.next is None:
                return False
            cur = cur.next
        if cur.next is None:
            return False
        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

        
