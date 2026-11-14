class Solution:
    def reverse(self, x: int) -> int:
        # if x[0]=='-'
        string = str(x)
        rev_string = string[::-1]
        if string[0]=='-':
            num = -int(rev_string[:-1])
        else:
            num = int(rev_string)
        # print(num)

        if num<pow(-2,31) or num>(pow(2,31)-1):
            return 0

        return num