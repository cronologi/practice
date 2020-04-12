class DynamicArray:
    def __init__(self, size = 10):
        self.max_size = size
        self.list = [None]
        self.size = 0

    def add(self, element):
        if self.size >= self.max_size:
            self._resize()
        self.list[self.size] = element
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid Index")

        for element in range(index, self.size):
            self.list[element] = self.list[element + 1]

        self.size -= 1    

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid Index")
        
        return self.list[index]

    def _resize(self):
        new_max_size = self.max_size * 2
        new_list = [None] * new_max_size

        for index in range(0, self.max_size):
            new_list[index] = self.list[index]
        
        self.max_size = new_max_size
        self.list = new_list