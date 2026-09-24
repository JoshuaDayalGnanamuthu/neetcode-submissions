class MedianFinder:

    def __init__(self):
        self.data = []
        
    def insertIndex(self, num: int) -> int:
        if (len(self.data) == 0): 
            return 0

        low = 0
        high = len(self.data) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.data[mid] == num:
                return mid 
            elif self.data[mid] < num:
                low = mid + 1 
            else:
                high = mid - 1 
                
        return low

    def addNum(self, num: int) -> None:
        index = self.insertIndex(num)
        self.data.insert(index, num)
        
        
    def findMedian(self) -> float:
        size = len(self.data)
        if (size % 2 == 1):
            return float(self.data[size // 2])
        
        index1 = size // 2
        index2 = (size - 1) // 2

        return (self.data[index1] + self.data[index2]) / 2


        
        