class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        mapping ={}
        ans = 0
        max_freq= 0
        for i in tasks:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1

            max_freq = max(max_freq, mapping[i])
        max_freq_task = 0

        for i,j in mapping.items():
            if j==max_freq:
                max_freq_task+=1


        return max((max_freq-1)*(n+1)+max_freq_task, len(tasks))











        