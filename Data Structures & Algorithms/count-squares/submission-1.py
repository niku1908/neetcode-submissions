class CountSquares:

    def __init__(self):
        self.mapping = {}
        self.mapping_points = {}

    def add(self, point: List[int]) -> None:
        point = (point[0],point[1])
        if point in self.mapping:
            self.mapping[point]+=1
        else:
            self.mapping[point]=1

        x,y = point
        if x in self.mapping_points:
            if y not in self.mapping_points[x]:
                self.mapping_points[x].append(y)
        else:
            self.mapping_points[x]=[y]

        # print(self.mapping)
        # print(self.mapping_points)

    def count(self, point: List[int]) -> int:
        result = 0
        x,y = point[0],point[1]
        if x in self.mapping_points:
            for i in self.mapping_points[x]:
                # ans = 1
                dis = abs(y-i)
                if dis==0:
                    continue
                
                if (x-dis,y) in self.mapping and (x-dis,i) in self.mapping:

                    
                    result+=(self.mapping[(x,i)]*self.mapping[(x-dis,y)]*self.mapping[(x-dis,i)])

                if (x+dis,y) in self.mapping and (x+dis,i) in self.mapping:
                    result+=(self.mapping[(x,i)]*self.mapping[(x+dis,y)]*self.mapping[(x+dis,i)])
                    
        return result







