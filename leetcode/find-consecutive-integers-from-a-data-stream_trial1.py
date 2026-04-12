from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.stack = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.stack.append(num)
        if num == self.value:
            self.count += 1


        if len(self.stack) > self.k:
            popped = self.stack.popleft()
            if popped == self.value:
                self.count -= 1


        if len(self.stack) < self.k:
            return False

        return self.count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)