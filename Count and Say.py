class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
    
        prev_res = '1'    
        for _ in range(2,n+1):
            s = ''
            c = 0
            element = prev_res[0]
            for j in str(prev_res):
                if j==element:
                    c+=1
                else:
                    s=s+str(c)+str(element)
                    element = j
                    c=1
            s=s+str(c)+str(element)
            prev_res = s
        return s
        
