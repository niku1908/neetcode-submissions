class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seti = set()
        for i in nums:
            if i in seti:
                return True
            seti.add(i)

        return False