class Solution:
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            x = str(x)
            if x[0]=="-": temp = -int(x[:0:-1])
            else:         temp = int(x[::-1])
            if temp >= 2**31-1 or temp <= -2**31: return 0
            return temp
        