class Solution():
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s) - 1):
            if s[i: i+2] == '++':
                res.append(s[:i] + '--' + s[i+2:])
        return res
    
    def canWin(self, s):
        for i in range(len(s) - 1):
            if s[i: i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                return True
        return False 