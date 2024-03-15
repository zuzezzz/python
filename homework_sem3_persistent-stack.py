class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = Node('head')

    def __str__(self):
        out = ''
        sep = ' ➤ '
        cur = self.head.next
        while cur:
            out += f'{cur.value}{sep}'
            cur = cur.next
        out = out[:-3]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        tmp = self.head.next.value
        self.head.next = self.head.next.next
        return tmp


def list_to_stack(lst):
    new_stack = Stack()
    for i in lst:
        new_stack.push(i)
    return new_stack


class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        super().__init__()

    def backup(self):
        copy = []
        current = self.head.next
        while current:
            copy.append(current)
            current = current.next
        self.backups.append(list_to_stack(copy))

        def get_backup(self, i):
            return self.backups[i]

        def print_backup(self, i):
            return print(str(self.get_backup(i)))

        def push(self, value):
            self.backup()
            super().push(value)

        def pop():
            self.backup()
            return super().pop()
