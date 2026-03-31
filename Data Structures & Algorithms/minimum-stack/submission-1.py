class MinStack:

    def __init__(self):
        self.vals = []
        self.minSoFar = []
        #self.smallestVal = None
        

    def push(self, val: int) -> None:
        self.vals.append(val)
        if not self.minSoFar: self.minSoFar.append(val)
        elif val < self.minSoFar[-1]: self.minSoFar.append(val)
        else: self.minSoFar.append(self.minSoFar[-1])
        #print(f"self.vals = {self.vals}")

    def pop(self) -> None:
        #if len(self.vals) == 0: return None
        self.vals.pop()
        self.minSoFar.pop()
        

    def top(self) -> int:
        return self.vals[len(self.vals)-1]
        

    def getMin(self) -> int:
        if not self.vals: return None
        return self.minSoFar[-1]