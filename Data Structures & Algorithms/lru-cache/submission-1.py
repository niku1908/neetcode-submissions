class LRUCache:

    def __init__(self, capacity: int):
      
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        

    
    def get(self, key: int) -> int:
       
        if key in self.cache:
            self.count+=1
            self.cache[key][1]=(self.count)
            return self.cache[key][0]
        return -1
        
    def remove_least_used(self):
        lru = []
        for i,j in self.cache.items():
            lru.append((j[1], i))

        lru.sort()
        key = lru[0][1]
        del self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.count+=1
        if key in self.cache:
            self.cache[key][0]=value
            self.cache[key][1]=(self.count)

        else:
            if len(self.cache)<self.capacity:
                self.cache[key]=[value, self.count]
            else:
                self.remove_least_used()
                self.cache[key]=[value, self.count]

        # print(self.cache)
