def check(res):
    print(res)
    if (len(res) == 0) or (len(res) == 1 and res[0] in '+-'):
        return 0
    max = pow(2,31)* (-1) if res[0] == '-' else pow(2,31)-1
    if res[0] == '-':
        if int(res) < max:
            return max
        else:
            return int(res)
    else:
        if int(res) > max:
            return max
        else:
            return int(res)
    
        
class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip(' ')
        res = ""
        dig = False
        for i in s:
            if i in '+-':
                if dig == False and len(res) == 0:
                    res += i
                    dig = True
                else:
                    return check(res)
            elif i.isnumeric():
                res+=i
            else:
                return check(res)
        return check(res)
