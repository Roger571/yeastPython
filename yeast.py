import time, math

class yeastManager():
    def __init__(self):
        self.szAlphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
        self.aMap  = {self.szAlphabet[i]: i for i in range(len(self.szAlphabet))}
        self.iLength = 64
        self.currentTime = lambda: int(round(time.time() * 1000))
        
    def decode(self, szString):
        iDecoded = 0
        for char in szString:
            iDecoded = iDecoded * self.iLength + self.aMap[char]
        return iDecoded
        
    def encode(self, iTime):
        szEncoded = ""
        while (iTime > 0):
            szEncoded = self.szAlphabet[int(iTime % self.iLength)] + szEncoded
            iTime = math.floor(iTime / self.iLength)
        return szEncoded
    
    def getCurrentEncode(self):
        return self.encode(self.currentTime())
