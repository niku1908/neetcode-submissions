class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            lst = list(i)
            lst.sort()
            string = "".join(lst)

            if string in dic:
                dic[string].append(i)
            else:
                dic[string]=[i]

        ans = []

        for i,j in dic.items():
            ans.append(j)
        return ans
