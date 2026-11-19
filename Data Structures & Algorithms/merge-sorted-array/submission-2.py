class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
            return

        i = m-1
        k = n+m-1
        j = n-1

        while i>=0 and j>=0:

            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1

            elif nums1[i]<=nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        if j>=0:
            while k>=0:
                nums1[k]=nums2[j]
                k-=1
                j-=1
