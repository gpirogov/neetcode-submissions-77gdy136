class MinStack:

    def __init__(self):
        self.vals = []
        

    def push(self, val: int) -> None:
        self.vals.append(val)
        print(f"self.vals = {self.vals}")

    def pop(self) -> None:
        if len(self.vals) == 0: return None
        self.vals.pop()
        

    def top(self) -> int:
        return self.vals[len(self.vals)-1]
        

    def getMin(self) -> int:
        # can be made O(1) if add a new object that keeps track of largest number 
        # ^ on other hand removing arbitrary element from the stack necessistates O(n) re-ordering of that object
        
        biggestVal = None if len(self.vals) == 0 else self.vals[0]
        
        for i in self.vals:
            if i < biggestVal: biggestVal = i
        return biggestVal