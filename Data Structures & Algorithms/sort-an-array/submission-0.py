class Solution:

    def merge_sorted_array(self, nums, left, mid, right):

        nums_left = nums[left:mid+1]
        nums_right = nums[mid+1:right+1]

        i,j,k = 0,0, left

        while i<len(nums_left) and j<len(nums_right):

            if nums_left[i]<=nums_right[j]:
                nums[k]=nums_left[i]
                i+=1
            else:
                nums[k]=nums_right[j]
                j+=1

            k+=1

        while i<len(nums_left):
            nums[k]= nums_left[i]
            i+=1
            k+=1

        while j<len(nums_right):
            nums[k]=nums_right[j]
            j+=1
            k+=1
            


    def mergesort(self, nums, left, right):

        if left>=right:
            return

        mid = left+(right-left)//2

        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid+1,right)

        self.merge_sorted_array(nums,left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.mergesort(nums, 0, len(nums)-1)

        return nums