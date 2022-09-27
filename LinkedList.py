class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self) -> None:
        self.headNode = None
