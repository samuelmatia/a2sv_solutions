from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = deque()
        

    def ping(self, t: int) -> int:
        self.counter.append(t)
        if self.counter :
            while self.counter[0] < t-3000 : 
                popped = self.counter.popleft()

        return len(self.counter)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)