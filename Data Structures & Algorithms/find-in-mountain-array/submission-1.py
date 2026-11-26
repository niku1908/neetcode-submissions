class Solution:
    def findInMountainArray(self, target: int, mount: 'MountainArray') -> int:
        
        
        n = mount.length()
        i = 0
        j = n-1

        # find peak

        while i<j:
            mid = (i+j)//2

            if mount.get(mid)<mount.get(mid+1):
                i = mid+1
            else:
                j = mid

        peak = i

        # left to peak

        i = 0
        j = peak
        
        while i<=j:
            mid = (i+j)//2
            if mount.get(mid)==target:
                return mid
            elif mount.get(mid)<target:
                i = mid+1
            else:
                j = mid-1
        
        i = peak+1
        j = n-1
        
        while i<=j:
            mid = (i+j)//2
            if mount.get(mid)==target:
                return mid
            elif mount.get(mid)<target:
                j = mid-1
            else:
                i = mid+1
            

        
        return -1