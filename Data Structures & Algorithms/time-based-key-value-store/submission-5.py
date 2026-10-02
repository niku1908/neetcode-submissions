class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping:
            self.mapping[key].append((timestamp, value))
            # self.mapping[key].sort()
        else:
            self.mapping[key]=[(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mapping:
           
            ans = 0
            low = 0
            high = len(self.mapping[key])-1

            while(low<=high):
                mid = (low+high)//2
                if self.mapping[key][mid][0]==timestamp:
                    ans = self.mapping[key][mid][1]
                    return ans

                elif self.mapping[key][mid][0]<timestamp:
                    low = mid+1
                    ans = self.mapping[key][mid][1]
                else:
                    high = mid-1

                
            if ans==0:
                ans = ""
                
        else:
            ans =""

        return ans

